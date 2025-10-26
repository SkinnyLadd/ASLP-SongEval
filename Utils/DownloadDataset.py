from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="ASLP-lab/Data",
    repo_type="dataset",
    local_dir="../Data",
    resume_download=True,
    token=""  # HuggingFace Token (optional but recommended) - Get your own from the HuggingFace Website :3
)

'''
Make sure the data gets downloaded into the correct directory - Execute in some other directory if unsure 
'''