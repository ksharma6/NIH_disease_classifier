import os
import torch, torchvision
import pandas as pd

class Dataset:
    def __init__(self, root_dir, img_dir,label_dir, label_col, transform=None):
        self.root_dir = root_dir
        self.transform= transform
        self.img_dir = img_dir
        self.img_paths= [self.root_dir + self.img_dir + f for f in os.listdir(self.root_dir + self.img_dir) if os.path.isfile(os.path.join(root_dir + img_dir, f))]
        
        
        temp = pd.read_csv(root_dir + label_dir)
       
        self.labels = temp[label_col].tolist()

    
    def __len__(self):
        return len(self.img_paths)

    def __getitem__(self, idx):
        img = torchvision.io.read_image(self.img_paths[idx])
        label = self.labels[idx]
        
        if self.transform:
            img = self.transform(img)
        
        sample = {'image': img,
                  'image_index':self.img_paths[idx],
                  'label': label}
        return sample






####test####
root = "/home/kishen/documents/projects/python_projects/nih_chest_xrays/data/"
test = Dataset(root_dir= root,
                img_dir= "images/",
                label_dir="labels.csv",
                label_col="Finding Labels")
print(test.__getitem__(1))
