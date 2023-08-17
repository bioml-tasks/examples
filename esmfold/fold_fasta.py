import os
from pathlib import Path

import bioml_tasks

# Get the directory of the script
script_dir = Path(__file__).parent

# Construct the full path to the file
filename = Path(script_dir / "data/example.fasta")

with open(filename, "rb") as f:
    res = bioml_tasks.run(
        "vivek/esmfold",
        "fold_fasta",
        files={"fasta": f},
        num_recycles=4,
        max_tokens_per_batch=1024,
    )

print(res)
# [
#     {
#         "name": "seq1",
#         "sequence": "MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG",
#         "pdb_string": "...",
#         "mean_plddt": 88.27366638183594,
#         "ptm": 0.8401376008987427,
#     },
#     {
#         "name": "seq2",
#         "sequence": "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE",
#         "pdb_string": "...",
#         "mean_plddt": 82.7134780883789,
#         "ptm": 0.8045980930328369,
#     },
# ]
