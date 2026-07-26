## Description: <br>
Fizzy helps an agent manage Fizzy boards, cards, steps, comments, reactions, users, tags, notifications, and related CLI workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[portavion](https://clawhub.ai/user/portavion) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, project operators, and agents use this skill to inspect and update Fizzy project-management workspaces through the Fizzy CLI. It supports board, card, step, comment, reaction, tag, user, notification, upload, pagination, and JSON parsing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete Fizzy workspace data when an agent has write-capable credentials. <br>
Mitigation: Use least-privilege Fizzy tokens, protect any token or config file, and confirm exact board, card, comment, upload, download, delete, read-all, and other write targets before execution. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and jq patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may return JSON responses and may read or modify Fizzy workspace data depending on credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
