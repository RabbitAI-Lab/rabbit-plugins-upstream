## Description: <br>
Search, download, and explore datasets from Kaggle, Hugging Face, UCI ML Repository, and Data.gov, with support for previews, local dataset management, and generated data cards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anisafifi](https://clawhub.ai/user/anisafifi) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Developers and data practitioners use this skill to find datasets for machine learning projects, download them from supported repositories, inspect local files, and generate dataset documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dataset search and download operations use network services and may require Kaggle or Hugging Face credentials. <br>
Mitigation: Install in a virtual environment, keep tokens out of source control and logs, and use dedicated project directories for downloads. <br>
Risk: Downloaded datasets and preview outputs may contain sensitive or raw sample rows. <br>
Mitigation: Review preview reports and generated data cards before sharing them, and check source dataset licenses and terms before use. <br>
Risk: Dependencies and downloaded files introduce normal local-file and package maintenance risk. <br>
Mitigation: Keep dependencies updated or pinned to patched versions and review downloaded files before using them in downstream workflows. <br>


## Reference(s): <br>
- [Dataset Finder reference readme](references/readme.md) <br>
- [Kaggle API](https://github.com/Kaggle/kaggle-api) <br>
- [Hugging Face Datasets documentation](https://huggingface.co/docs/datasets/) <br>
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/) <br>
- [Data.gov APIs](https://www.data.gov/developers/apis) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Text, JSON, Markdown, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; command outputs may be text, JSON result files, downloaded dataset files, or Markdown data cards.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Kaggle or Hugging Face credentials and writes downloaded datasets, preview reports, or generated data cards to local paths selected by the user.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and artifact readme) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
