## Description:

Deepseek聊天 helps agents support Chinese DeepSeek-related chat workflows with configuration guidance, API-key setup notes, and basic troubleshooting for automation-oriented use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users can use this skill to guide Chinese-language DeepSeek chat setup, configuration, and troubleshooting in agent workflows. Review installation carefully because the server security assessment flags broad local read, write, and command execution capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security assessment marks the skill suspicious because it requests broad read, write, and command execution capabilities without clear use limits.

Mitigation: Install only when those local capabilities are intentionally needed, review the skill before use, and prefer a narrower chat/API skill when local file or command access is unnecessary.

Risk: API-key guided workflows can expose credentials if copied into logs, shell history, or shared workspaces.

Mitigation: Use environment variables or a secret manager, keep keys out of version control, and rotate credentials if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/deepseek-chat)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub homepage from skill metadata](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and JSON-shaped result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key when used for DeepSeek-related API workflows; evidence provenance is unavailable for this release.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
