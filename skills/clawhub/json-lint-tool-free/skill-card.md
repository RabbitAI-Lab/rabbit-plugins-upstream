## Description: <br>
JSON校验工具免费版 helps agents recursively scan local workspace .json files, validate strict JSON syntax, and produce structured syntax error reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and data teams use this skill to check workspace JSON files before commits, deployments, configuration audits, or data-file handoff. The skill reports invalid files with paths, error messages, and line or column details so users can fix syntax issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recursive workspace scanning can include sensitive, generated, dependency, or very large folders. <br>
Mitigation: Run the skill only on a clearly selected project directory and configure exclusions for sensitive paths, dependency folders, build outputs, and unusually large directories. <br>
Risk: The release declares exec and write authority even though the core behavior is reporting-oriented JSON validation. <br>
Mitigation: Review proposed shell commands and file writes before execution, and prefer read-only report generation unless a write is explicitly needed. <br>
Risk: The security summary notes unrelated broad triggers in the metadata, which may cause the skill to be selected outside its intended JSON validation task. <br>
Mitigation: Invoke it only for local JSON syntax validation and ignore it for unrelated data analysis, deployment, or machine learning requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/json-lint-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and structured JSON, text, or CSV report output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include scan timestamps, file counts, pass rate, invalid file paths, parser error messages, and line or column locations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
