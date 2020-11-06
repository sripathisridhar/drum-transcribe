import numpy as np
import os
import glob

DATA_DIR = "/Users/sripathisridhar/mir_datasets/idmt_smt_realdrums/dataset"

data_paths = glob.glob(os.path.join(DATA_DIR, 'SD*.wav'))

file_names = []
for path in data_paths:
    file_names.append(os.path.basename(path))

print(len(file_names))
