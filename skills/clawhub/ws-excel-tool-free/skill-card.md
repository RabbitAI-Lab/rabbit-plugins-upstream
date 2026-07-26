## Description: <br>
Ws Excel Tool Free helps agents read, write, clean, calculate formulas in, and summarize xlsx files without requiring Microsoft Excel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, individual analysts, and developers use this skill to have an agent process user-provided xlsx files for basic reading, writing, data cleaning, formulas, formatting, and summary statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may run local Python code against Excel files supplied by the user. <br>
Mitigation: Use it only on files you intend the agent to process, and review the generated Python or shell commands before execution. <br>
Risk: The skill may write or overwrite local Excel output files. <br>
Mitigation: Ask the agent to show the resolved output path first and to create new filenames unless an overwrite is explicitly requested. <br>
Risk: Data cleaning, formula insertion, or formatting changes can alter spreadsheet contents in ways that affect downstream decisions. <br>
Mitigation: Keep an original copy of the workbook and review formulas, row counts, and summary statistics before relying on the processed output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ws-excel-tool-free) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with Python code snippets, shell commands, generated Excel files, and JSON-style status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local Excel files supplied by the user and may write new xlsx outputs to a requested path or workspace data directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
