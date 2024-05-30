import torch
import numpy as np
import random

def set_seed(seed=42):
    torch.manual_seed(seed)
    if torch.cuda.is_available():    
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    # torch.backends.cudnn.deterministic = True
    # torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)

__all__ = [
    "set_seed",
]