import shutil, os

source_name = "AnimalFace-dog"
target_name = "Dog"

source_path = f"/home/chaerin/research/CLAE/few-shot-images/{source_name}/img/"
target_path  = f"/home/chaerin/research/Dataset/30-shot/{target_name}/img/"

import random

n_shots = 30

files = os.listdir(source_path)

chosen_files = random.sample(files, k=n_shots)

for f in chosen_files:
    shutil.copyfile(source_path+f, target_path+f)


