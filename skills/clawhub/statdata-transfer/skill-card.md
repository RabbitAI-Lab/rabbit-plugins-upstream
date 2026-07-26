## Description: <br>
Read and convert 50+ statistical software and clinical trial data formats into Python/pandas, preserving variable labels, value labels, and missing-value metadata where the source format supports them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data engineers, statisticians, and clinical data teams use this skill to inspect, read, and convert statistical datasets across formats such as SPSS, Stata, SAS, R, Excel, Parquet, HDF5, JSON, and CSV while surfacing metadata-loss warnings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional environment setup can modify the local Python environment when package installation is explicitly requested. <br>
Mitigation: Run environment checks without installation by default and use `python scripts/check_env.py --install` only in an environment where dependency changes are acceptable. <br>
Risk: Some R-backed formats can invoke a local R interpreter when `allow_r_exec=True` is enabled for trusted files. <br>
Mitigation: Keep R execution disabled for untrusted files and prefer pure-Python parsing paths for sensitive or unknown datasets. <br>
Risk: The opt-in R bridge may briefly materialize converted data in a temporary CSV file. <br>
Mitigation: Avoid R-backed conversion paths for highly sensitive data unless the working environment and temporary-file handling are acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/statdata-transfer) <br>
- [Project Homepage](https://github.com/medstatstar/statdata-transfer) <br>
- [README](artifact/README.md) <br>
- [Chinese README](artifact/README_ZH.md) <br>
- [Usage Examples](artifact/references/usage_examples.py) <br>
- [New Formats Architecture Analysis](artifact/references/new_formats_architecture_analysis.json) <br>
- [Version 1.4 Implementation Summary](artifact/references/v1.4_implementation_summary.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, and structured conversion results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce pandas DataFrames, metadata dictionaries, warning lists, and converted data files when used with local files.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
