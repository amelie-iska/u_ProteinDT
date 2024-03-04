import os
import shutil

data_folder_dict = {
    "latent_interpolation": [
        "/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_RNN_lr_1e-5_hidden_16_e_10_unconditional_0/downstream_Editing_latent_interpolation_{}/prompt_{}_theta_0.5_num_repeat_16_simplified_oracle_protein",
        "/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_04_MultinomialDiffusion_BertBase_lr_1e-5_hidden_32_e_10_unconditional_0/downstream_Editing_latent_interpolation_{}/prompt_{}_theta_0.9_num_repeat_16_simplified_oracle_text",
        "/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/ProtBERT_BFD-512-1e-5-1-text-512-1e-5-1-EBM_NCE-1-batch-9-gpu-8-epoch-10/step_04_T5Decoder_T5Base_lr_1e-4_hidden_16_e_10_unconditional_0/downstream_Editing_latent_interpolation_{}/prompt_{}_theta_0.9_num_repeat_16_oracle_text_inference_01_expanded",
    ],
    "latent_optimization": [
        "/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/ProtBERT_BFD-512-1e-5-1e-1-text-512-1e-5-1e-1-EBM_NCE-0.1-batch-9-gpu-8-epoch-5/step_05_AE_1e-3_3/downstream_Editing_latent_optimization/{}_prompt_{}_lambda_0.9_num_repeat_16_oracle_text_T_2",
    ],
}


if __name__ == "__main__":
    # First copy peptide-binding editing results for docking visualization
    method_list = ["latent_interpolation", "latent_optimization"]
    editing_task = "peptide_binding"
    prompt_idx_list = [101, 201]
    for method_idx, method in enumerate(method_list):
        folder_template_list = data_folder_dict[method]

        for folder_idx, folder_template in enumerate(folder_template_list):
            for prompt_idx in prompt_idx_list:
                old_folder_ = folder_template.format(editing_task, prompt_idx)

                neo_folder = old_folder_.replace("/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/", "")

                # # os.makedirs(neo_folder, exist_ok=True)
                shutil.copytree(old_folder_, neo_folder)

    # Then copy structure editing results
    method_list = ["latent_interpolation", "latent_optimization"]
    editing_task_list = ["alpha", "beta"]

    prompt_idx_list = [101, 201]
    for method_idx, method in enumerate(method_list):
        folder_template_list = data_folder_dict[method]
        for editing_task in editing_task_list:

            for folder_idx, folder_template in enumerate(folder_template_list):
                for prompt_idx in prompt_idx_list:
                    old_folder_ = folder_template.format(editing_task, prompt_idx)

                    neo_folder = old_folder_.replace("/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/", "")

                    # # os.makedirs(neo_folder, exist_ok=True)
                    shutil.copytree(old_folder_, neo_folder)

    # Lastly, copy stability editing results
    method_list = ["latent_interpolation", "latent_optimization"]
    editing_task_list = ["Villin", "Pin1"]

    prompt_idx_list = [101, 102, 201, 202]
    for method_idx, method in enumerate(method_list):
        folder_template_list = data_folder_dict[method]
        for editing_task in editing_task_list:

            for folder_idx, folder_template in enumerate(folder_template_list):
                for prompt_idx in prompt_idx_list:
                    old_folder_ = folder_template.format(editing_task, prompt_idx)

                    neo_folder = old_folder_.replace("/gpfs/projects/AI4D/core-08/ProteinDT_workspace_1213_part2/ProteinDT_dev/output/ProteinDT/", "")

                    # # os.makedirs(neo_folder, exist_ok=True)
                    shutil.copytree(old_folder_, neo_folder)
