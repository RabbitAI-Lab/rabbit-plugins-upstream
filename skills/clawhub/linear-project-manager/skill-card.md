## Description:

Linear项目管理 wraps Linear project-management API interactions so an agent can help with project management, task planning, progress tracking, team collaboration, and structured API responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, independent builders, and teams use this skill to automate Linear-related project operations, task planning, progress tracking, collaboration workflows, and API response handling. It is not intended for actual personnel performance evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags broad local file and command authority with vague scoping.

Mitigation: Review before installing, grant these permissions only when needed for Linear/API automation, and prefer a narrowed version that removes unnecessary exec or write access.

Risk: The activation wording is broad and could trigger outside explicit Linear work.

Mitigation: Use the skill only for explicit Linear project-management requests and require confirmation before mutating project data or running commands.

Risk: API automation may expose credentials or sensitive project data if configured or logged carelessly.

Mitigation: Store API keys in environment variables, avoid committing credentials, and review output and logs for sensitive data before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/linear-project-manager)
- [Skill source homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and shell environment setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return API response data or error details; requires API key configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
