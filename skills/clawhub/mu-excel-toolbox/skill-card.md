## Description: <br>
Excel全能工具箱 helps agents preview, read, write, merge, split, clean, validate, analyze, chart, compare, template-fill, and protect Excel or CSV spreadsheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[muippt](https://clawhub.ai/user/muippt) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, business analysts, and developers use this skill through an agent to inspect, transform, validate, analyze, visualize, compare, and protect spreadsheet files for reporting, HR rosters, attendance, operations data, and template-based document generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read spreadsheet contents and print previews into logs or chats, including sensitive business, HR, payroll, or performance data. <br>
Mitigation: Use it only on intended files, avoid broad auto-routing for sensitive workbooks, and review previews before sharing outputs. <br>
Risk: The skill can write, overwrite, encrypt, or decrypt local workbooks. <br>
Mitigation: Use explicit output paths, confirm directories, keep independent backups, and verify generated files before replacing originals. <br>
Risk: First-run dependency installation can add Python packages to the local environment. <br>
Mitigation: Prefer manually installing pinned dependencies from requirements.txt in an isolated environment before running the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-excel-toolbox) <br>
- [Project landing page](https://muippt.github.io/mu-excel-toolbox/) <br>
- [API Reference](references/api-reference.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with shell commands; scripts can emit JSON, CSV, Markdown, terminal tables, and spreadsheet files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local file operations may read, write, encrypt, decrypt, preview, or transform spreadsheet contents.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata; frontmatter lists 1.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
