import bioml_tasks


res = bioml_tasks.run(
    "vivek/esmfold",
    "fold_sequences",
    seqs=[
        {
            "name": "seq1",
            "sequence": "MKTVRQERLKSIVRILERSKEPVSGAQLAEELSVSRQVIVQDIAYLRSLGYNIVATPRGYVLAGG",
        },
        {
            "name": "seq2",
            "sequence": "KALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEE",
        },
    ],
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
