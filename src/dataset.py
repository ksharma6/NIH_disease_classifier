import torch 
import pandas as pd

class Dataset:
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform= transform
        self.img_paths= None
        self.labels= pd.read_csv()

    
    def __len__(self):
        pass

    def __getitem__(self, idx):
        
        
        if self.transform:
            pass


