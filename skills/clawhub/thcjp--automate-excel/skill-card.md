## Description: <br>
Automates reading, writing, merging, transforming, and validating Excel and CSV files for spreadsheet conversion, filtering, aggregation, validation, and reporting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to automate local spreadsheet work, including merging sheets, converting Excel and CSV files, filtering rows, aggregating data, validating required columns, and generating reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides an agent to process local spreadsheet files and write Excel or CSV outputs. <br>
Mitigation: Confirm input and output paths before running commands, and avoid processing sensitive files unless that is the intended task. <br>
Risk: The skill may require installing and running common Python spreadsheet packages. <br>
Mitigation: Review proposed shell commands and install dependencies in a controlled environment before executing spreadsheet automation. <br>
Risk: The security evidence notes that referenced helper scripts were not included in this artifact. <br>
Mitigation: Verify any referenced script exists before relying on it, or use the documented Python, pandas, and openpyxl patterns directly. <br>


## Reference(s): <br>
- [Automate Excel ClawHub skill page](https://clawhub.ai/thcjp/skills/automate-excel) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to read local spreadsheet files and write Excel or CSV outputs after confirming paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter declares 0.1.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
