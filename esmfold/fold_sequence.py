import bioml_tasks


res = bioml_tasks.run(
    "vivek/esmfold",
    "fold_sequence",
    sequence="MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG",
    num_recycles=4,
)
print(res)
# {
#     "name": "MKTVRQERLKSIVRILERSKE", # name defaults to first 20 characters of sequence if not provided
#     "sequence": "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE",
#     "pdb_string": "...",
#     "mean_plddt": 88.27366638183594,
#     "ptm": 0.8401376008987427,
# },

res1 = bioml_tasks.run(
    "vivek/esmfold",
    "fold_sequence",
    name="seq1",
    sequence="KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE",
    num_recycles=4,
)
print(res1)
# {
#     "name": "seq1",
#     "sequence": "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE",
#     "pdb_string": "...",
#     "mean_plddt": 82.7134780883789,
#     "ptm": 0.8045980930328369,
# },
