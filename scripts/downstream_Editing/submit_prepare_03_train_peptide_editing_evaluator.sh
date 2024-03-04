cd ../../examples/downstream_Editing


epochs_list=(100 500 1000)
lr_list=(1e-4 5e-4 1e-3)


export time=23
export partition=xxx


for epochs in "${epochs_list[@]}"; do
for lr in "${lr_list[@]}"; do
    output_folder=datasets_and_checkpoints/peptide_binding/MISATO/lr_"$lr"_epochs_"$epochs"
    output_file="$output_folder"/output.txt

    mkdir -p "$output_folder"
    tail "$output_file"

    # sbatch --gres=gpu:1 -n 8 --mem 32G --nodes 1 -t "$time":59:00 --partition="$partition" --job-name=oracle_"$time" \
    # --output="$output_file" \
    # ./run_prepare_03_train_peptide_editing_evaluator.sh \
    # --epochs="$epochs" --lr="$lr" \
    # --output_model_dir="$output_folder" \

    echo
    echo
    echo

done
done
