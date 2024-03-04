from huggingface_hub import HfApi
from huggingface_hub import snapshot_download
from huggingface_hub import hf_hub_download


api = HfApi()

# api.upload_file(
#     path_or_fileobj="data/downstream_datasets.zip",
#     path_in_repo="downstream_datasets.zip",
#     repo_id="chao1224/ProteinDT",
#     repo_type="dataset",
# )



# api.upload_file(
#     path_or_fileobj="README_data.md",
#     path_in_repo="README.md",
#     repo_id="chao1224/ProteinDT",
#     repo_type="dataset",
# )



api.upload_file(
    path_or_fileobj="README_checkpoints.md",
    path_in_repo="README.md",
    repo_id="chao1224/ProteinDT",
    repo_type="model",
)


api.upload_folder(
    folder_path="output/ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5",
    path_in_repo="ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5",
    repo_id="chao1224/ProteinDT",
    allow_patterns=["*pth", "*bin", "*json", "step_02_pairwise_representation"],
    repo_type="model",
)


api.upload_folder(
    folder_path="output/ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-InfoNCE-0.1-batch-9-gpu-8-epoch-5",
    path_in_repo="ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-InfoNCE-0.1-batch-9-gpu-8-epoch-5",
    repo_id="chao1224/ProteinDT",
    allow_patterns=["*pth", "*bin", "*json", "step_02_pairwise_representation"],
    repo_type="model",
)


api.upload_folder(
    folder_path="output/ProteinDT/ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10",
    path_in_repo="ProteinDT/ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10",
    repo_id="chao1224/ProteinDT",
    allow_patterns=["*pth", "*bin", "*json", "step_02_pairwise_representation"],
    repo_type="model",
)



# api.upload_folder(
#     folder_path="examples/downstream_Editing/datasets_and_checkpoints",
#     path_in_repo="downstream_Editing/datasets_and_checkpoints",
#     repo_id="chao1224/ProteinDT",
#     repo_type="dataset",
# )
