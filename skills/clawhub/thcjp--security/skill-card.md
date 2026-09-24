## Description:

GoPlus安全扫描 helps agents scan Go code and dependencies for vulnerabilities, inspect findings, manage scheduled patrols, and send scan notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to run manual or scheduled security checks on Go projects, review vulnerability findings, and coordinate remediation through reports or notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation language may cause the skill to be used for unrelated automation tasks.

Mitigation: Use the skill only for explicit Go project security-scanning requests and review the planned action before execution.

Risk: The skill can propose command execution and scheduled patrol behavior that is underspecified in the artifact.

Mitigation: Require clear user approval before running commands or starting scheduled patrols, and keep execution in a controlled project workspace.

Risk: Webhook notifications may send scan summaries to external services.

Mitigation: Configure webhooks only when the destination is trusted and the team accepts sending scan summary data externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/security)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured scan summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vulnerability details, severity summaries, remediation guidance, webhook configuration, and report export guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
