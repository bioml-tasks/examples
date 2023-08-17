import os

import bioml_tasks

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the file
filename = os.path.join(script_dir, "data/example.fasta")

output_path = os.path.join(script_dir, "output/example.zip")

with open(filename, "rb") as f:
    res = bioml_tasks.run(
        "vivek/esmfold",
        "fold_fasta/zipped",
        files={"fasta": f},
        num_recycles=4,
        max_tokens_per_batch=1024,
    )

    with open(output_path, "wb") as f_out:
        # Process the response as a stream to avoid loading the entire file into memory if it is large
        for chunk in res.iter_content(chunk_size=8192):
            f_out.write(chunk)

    # Close the response object
    res.close()

# The f"output_path" zipped file will be a directory that contains a pdb file for each sequence
# it also includes a confidence_metrics.csv file that contains the mean pLDDT and pTM scores for each sequence
