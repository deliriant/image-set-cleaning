# trained model is located on NIPG13

# training set (images and metadata):
# /home/muhannad/diffusers/examples/text_to_image/imageset/train


# trained model and training script locations:
# /home/muhannad/diffusers/examples/text_to_image

# required exports:
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/muhannad/.local/bin
export MODEL_NAME=CompVis/stable-diffusion-v1-4
export TRAIN_DIR=imageset/
export OUTPUT_DIR=trained-model/

# training script parameters:
accelerate launch train_text_to_image.py   --pretrained_model_name_or_path=$MODEL_NAME   --train_data_dir=$TRAIN_DIR   --use_ema --resolution=256 --center_crop --random_flip   --train_batch_size=1   --gradient_accumulation_steps=4   --gradient_checkpointing   --mixed_precision="fp16"   --max_train_steps=15000   --learning_rate=1e-05   --max_grad_norm=1   --lr_scheduler="constant" --lr_warmup_steps=0   --output_dir=${OUTPUT_DIR} --checkpointing_steps=3000


# image generation script:
# /home/muhannad/generate_image.py
# example: python3 generate_image.py "prompt or caption" output-image.png