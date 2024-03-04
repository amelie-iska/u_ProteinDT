import os
import random
import argparse
import numpy as np
from tqdm import tqdm
import time

import torch
import torch.nn as nn

from transformers import AutoModel, AutoTokenizer
from transformers import BertModel, BertTokenizer
from torch.utils.data import DataLoader

from downstream_Retrieval_utils import TextProteinPairDataset
from protein.models import ProteinTextModel


@torch.no_grad()
def eval(dataloader, model, evaluation_T_list, device):
    protein_repr_list, text_repr_list = [], []
    for batch in dataloader:
        protein_sequence_input_ids = batch["protein_sequence_input_ids"].to(device)
        protein_sequence_attention_mask = batch["protein_sequence_attention_mask"].to(device)
        text_sequence_input_ids = batch["text_sequence_input_ids"].to(device)
        text_sequence_attention_mask = batch["text_sequence_attention_mask"].to(device)
        
        protein_repr, text_repr = model(protein_sequence_input_ids, protein_sequence_attention_mask, text_sequence_input_ids, text_sequence_attention_mask)
        protein_repr = protein_repr.detach().cpu().numpy()
        text_repr = text_repr.detach().cpu().numpy()

        protein_repr_list.append(protein_repr)
        text_repr_list.append(text_repr)

    protein_repr_list = np.concatenate(protein_repr_list)
    text_repr_list = np.concatenate(text_repr_list)
    
    similarity_matrix = np.matmul(protein_repr_list, text_repr_list.T)
    N = similarity_matrix.shape[0]

    accuracy_list = []
    for evaluation_T in evaluation_T_list:
        accuracy = 0
        for i in range(N):
            start, end = i, i + evaluation_T
            similarity_matrix_segment = []
            for j in range(start, end):
                similarity_matrix_segment.append(similarity_matrix[i][j % N])
            optimal_index = np.argmax(similarity_matrix_segment)
            accuracy += (optimal_index == 0)
        accuracy = accuracy * 100. / N
        accuracy_list.append(accuracy)
    return accuracy_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--num_workers", type=int, default=8)
    parser.add_argument("--dataset_size", type=int, default=200)

    parser.add_argument("--input_text_file_path", type=str, default="temp_step_02_output.txt")
    parser.add_argument("--pretrained_folder", type=str, default=None)

    parser.add_argument("--verbose", dest="verbose", action="store_true")
    parser.set_defaults(verbose=False)

    parser.add_argument("--SSL_emb_dim", type=int, default=256)

    parser.add_argument("--protein_backbone_model", type=str, default="ProtBERT", choices=["ProtBERT", "ProtBERT_BFD"])
    parser.add_argument("--protein_max_sequence_len", type=int, default=512)
    parser.add_argument("--text_max_sequence_len", type=int, default=512)

    args = parser.parse_args()
    print("arguments", args)
    assert args.pretrained_folder is not None
    step_01_folder = args.pretrained_folder

    random.seed(args.seed)
    os.environ['PYTHONHASHSEED'] = str(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True
    
    device = torch.device("cuda:" + str(args.device)) if torch.cuda.is_available() else torch.device("cpu")
    
    ##### Load pretrained protein model
    if args.protein_backbone_model == "ProtBERT":
        protein_tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert", do_lower_case=False, chache_dir="../../data/temp_pretrained_ProtBert")
        protein_model = BertModel.from_pretrained("Rostlab/prot_bert", cache_dir="../../data/temp_pretrained_ProtBert")
    elif args.protein_backbone_model == "ProtBERT_BFD":
        protein_tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert_bfd", do_lower_case=False, chache_dir="../../data/temp_pretrained_ProtBert_BFD")
        protein_model = BertModel.from_pretrained("Rostlab/prot_bert_bfd", cache_dir="../../data/temp_pretrained_ProtBert_BFD")
    protein_dim = 1024
    input_model_path = os.path.join(args.pretrained_folder, "protein_model.pth")
    print("Loading protein model from {}...".format(input_model_path))
    state_dict = torch.load(input_model_path, map_location='cpu')
    protein_model.load_state_dict(state_dict)

    ##### Load pretrained text model
    text_tokenizer = AutoTokenizer.from_pretrained('allenai/scibert_scivocab_uncased', cache_dir="../../data/temp_pretrained_SciBert")
    text_model = AutoModel.from_pretrained('allenai/scibert_scivocab_uncased', cache_dir="../../data/temp_pretrained_SciBert")
    text_dim  = 768
    input_model_path = os.path.join(args.pretrained_folder, "text_model.pth")
    print("Loading text model from {}...".format(input_model_path))
    state_dict = torch.load(input_model_path, map_location='cpu')
    text_model.load_state_dict(state_dict)

    ##### Load pretrained protein2latent model
    protein2latent_model = nn.Linear(protein_dim, args.SSL_emb_dim)
    input_model_path = os.path.join(args.pretrained_folder, "protein2latent_model.pth")
    print("Loading protein2latent model from {}...".format(input_model_path))
    state_dict = torch.load(input_model_path, map_location='cpu')
    protein2latent_model.load_state_dict(state_dict)

    ##### Load pretrained text2latent model
    text2latent_model = nn.Linear(text_dim, args.SSL_emb_dim)
    input_model_path = os.path.join(args.pretrained_folder, "text2latent_model.pth")
    print("Loading text2latent model from {}...".format(input_model_path))
    state_dict = torch.load(input_model_path, map_location='cpu')
    text2latent_model.load_state_dict(state_dict)

    model = ProteinTextModel(protein_model, text_model, protein2latent_model, text2latent_model)
    model.eval()
    model.to(device)

    dataset = TextProteinPairDataset(
        data_path=args.input_text_file_path,
        protein_tokenizer=protein_tokenizer,
        text_tokenizer=text_tokenizer,
        protein_max_sequence_len=args.protein_max_sequence_len,
        text_max_sequence_len=args.text_max_sequence_len)
    dataloader = DataLoader(dataset, batch_size=args.batch_size, shuffle=False, num_workers=args.num_workers)

    evaluation_T_list = [4, 10]
    accuracy_list = eval(dataloader, model, evaluation_T_list, device)
    for evaluation_T, accuracy in zip(evaluation_T_list, accuracy_list):
        print("evaluation_T: {}\taccuracy: {}".format(evaluation_T, accuracy))
