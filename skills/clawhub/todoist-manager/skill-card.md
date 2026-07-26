## Description: <br>
Manage Todoist tasks, projects, labels, and comments via the todoist CLI wrapper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreisuslov](https://clawhub.ai/user/andreisuslov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Todoist users use this skill to manage Todoist tasks, projects, sections, labels, and comments from an agent through a Todoist CLI wrapper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Todoist API token. <br>
Mitigation: Treat the token like a password, store it in a temporary environment variable or secret manager, and rotate it if exposure is suspected. <br>
Risk: The documented workflow includes live delete operations for tasks, projects, sections, labels, and comments. <br>
Mitigation: Verify IDs before mutations and require explicit user confirmation before running delete commands. <br>
Risk: The referenced todoist CLI helper is not included for inspection in the artifact. <br>
Mitigation: Install only after inspecting or otherwise trusting the executable that receives the Todoist API token. <br>


## Reference(s): <br>
- [Todoist Manager on ClawHub](https://clawhub.ai/andreisuslov/skills/todoist-manager) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Todoist CLI commands return JSON and can be piped to jq.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
