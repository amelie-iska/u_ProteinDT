folder_list=(
    ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5
    ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-InfoNCE-0.1-batch-9-gpu-8-epoch-5
    ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10
)


for folder in "${folder_list[@]}"; do
    echo "$folder"
    mkdir -p "$folder"

    # cp /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/*pth     ./"$folder"/
    # cp -r /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/step_02*     ./"$folder"/
    # cp -r /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/step_03*     ./"$folder"/

    # # cp -r /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/step_04*     ./"$folder"/
    # # cp -r /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/step_05*     ./"$folder"/

    # cp -r /gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/"$folder"/downstream_TAPE     ./"$folder"/
    # rm -rf ./"$folder"/downstream_TAPE/ss8/3-3e-5-5-2-16-0.08
    # rm -rf ./"$folder"/downstream_TAPE/contact/3-3e-5-10-1-1-0.08
    # rm -rf ./"$folder"/downstream_TAPE/remote_homology/3-3e-5-10-1-64-0.08
    # rm -rf ./"$folder"/downstream_TAPE/stability/3-3e-5-1-2-16-0.08
    # rm -rf ./"$folder"/downstream_TAPE/stability/3-3e-5-3-2-16-0.08
    # rm -rf ./"$folder"/downstream_TAPE/fluorescence/3-3e-5-25-8-8-0.0-True

done

# rm -rf ./ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/downstream_TAPE













########## downstream: Text2Protein ##########

export COPY=/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT


# # ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0.1/downstream_Retrieval/num_repeat_16_use_prior_inference_01/step_02_inference.out
# # ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0.1/downstream_Retrieval/num_repeat_16_no_use_prior_inference_01/step_02_inference.out


# step_04_folder=ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0.1
# mkdir -p "$step_04_folder"/downstream_Text2Protein
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_use_prior_inference_01       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_use_facilitator_inference_01
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_no_use_prior_inference_01       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_no_facilitator_inference_01



# ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-4_hidden_32_e_10_unconditional_0/downstream_Retrieval/num_repeat_16_use_prior_simplified/step_02_inference.out
# ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-4_hidden_32_e_10_unconditional_0/downstream_Retrieval/num_repeat_16_no_use_prior_simplified/step_02_inference.out


# step_04_folder=ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-4_hidden_32_e_10_unconditional_0
# mkdir -p "$step_04_folder"/downstream_Text2Protein
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_use_prior_simplified       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_use_facilitator_simplified
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_no_use_prior_simplified       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_no_facilitator_prior_simplified





# # ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_MultinomialDiffusion_BertBase_lr_1e-4_hidden_32_e_10_unconditional_0/downstream_Retrieval/num_repeat_16_use_prior_simplified/step_02_inference.out
# # ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_MultinomialDiffusion_BertBase_lr_1e-4_hidden_32_e_10_unconditional_0/downstream_Retrieval/num_repeat_16_no_use_prior_simplified/step_02_inference.out


# step_04_folder=ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_MultinomialDiffusion_BertBase_lr_1e-4_hidden_32_e_10_unconditional_0
# mkdir -p "$step_04_folder"/downstream_Text2Protein
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_use_prior_simplified       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_use_facilitator_simplified
# cp -r "$COPY"/"$step_04_folder"/downstream_Retrieval/num_repeat_16_no_use_prior_simplified       "$step_04_folder"/downstream_Text2Protein/num_repeat_16_no_facilitator_prior_simplified














########## downstream: Protein Editing ##########
export COPY=/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT


# ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-5_hidden_16_e_10_unconditional_0
# ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_BertBase_lr_1e-5_hidden_32_e_10_unconditional_0
# ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0
# ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_05_AE_1e-3_3


# step_04_folder=ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-5_hidden_16_e_10_unconditional_0
# mkdir -p "$step_04_folder"
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/


# step_04_folder=ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_BertBase_lr_1e-5_hidden_32_e_10_unconditional_0
# mkdir -p "$step_04_folder"
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/


# step_04_folder=ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0
# mkdir -p "$step_04_folder"
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/


# step_04_folder=ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_05_AE_1e-3_3
# mkdir -p "$step_04_folder"
# cp "$COPY"/"$step_04_folder"/* "$step_04_folder"/
