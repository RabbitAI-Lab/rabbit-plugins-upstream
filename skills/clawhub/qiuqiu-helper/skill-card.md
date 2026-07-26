## Description: <br>
Automates workspace tasks including summarizing recent changes, adding timestamped notes, and cleaning old log files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mmogdeveloper](https://clawhub.ai/user/mmogdeveloper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and workspace users use this skill to summarize recent workspace state, append quick timestamped notes to memory files, and remove old log files with configurable retention settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Deleting logs from an overly broad or incorrect directory could remove files the user intended to keep. <br>
Mitigation: Confirm the clean_logs target path and retention period before running it, and restrict use to dedicated log directories. <br>
Risk: Quick notes can store sensitive information in memory files if the user includes it. <br>
Mitigation: Avoid saving secrets or sensitive personal data in quick notes and review the destination file when needed. <br>


## Reference(s): <br>
- [Qiuqiu Helper ClawHub page](https://clawhub.ai/mmogdeveloper/skills/qiuqiu-helper) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with parameterized workspace-task guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append timestamped notes to files and delete old log files according to user-specified path and retention parameters.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
