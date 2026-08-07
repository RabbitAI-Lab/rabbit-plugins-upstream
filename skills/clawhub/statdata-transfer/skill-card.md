## Description: <br>
Read and convert 50+ statistical and clinical-trial data formats while preserving variable labels, value labels, and missing-value metadata for binary statistical formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data analysts, and clinical data managers use this skill to inspect and convert SPSS, Stata, SAS, R, Excel, Parquet, JSON, CSV, and related statistical files while understanding which metadata will be preserved or lost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local data files and writes converted outputs, sidecar metadata, and possible .hyper backups. <br>
Mitigation: Review the planned input and output paths before execution and handle sensitive or regulated data according to local data-governance controls. <br>
Risk: R-backed conversions can invoke a local R interpreter for trusted files when explicitly enabled. <br>
Mitigation: Keep R-backed conversions disabled for untrusted or highly sensitive files and enable allow_r_exec only for trusted inputs. <br>
Risk: The optional environment checker can install missing Python packages when explicitly requested. <br>
Mitigation: Run optional package installation only in an intended environment, preferably an isolated virtual environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/medstatstar/skills/statdata-transfer) <br>
- [Project homepage](https://github.com/medstatstar/statdata-transfer) <br>
- [README](README.md) <br>
- [Chinese README](README_zh-CN.md) <br>
- [Usage examples](references/usage_examples.py) <br>
- [R project](https://cran.r-project.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with Python code snippets and shell commands; converted data files are written only when explicitly requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write converted files, sidecar metadata, and .hyper backup files when the user asks the agent to execute a conversion.] <br>

## Skill Version(s): <br>
2.2.1 (source: SKILL.md frontmatter, CHANGELOG, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
