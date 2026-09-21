## Description:

元安全 yotta-agent-hardening helps developers inspect an AI agent environment for prompt-injection exposure, tool-call boundary issues, and data-isolation risks, then produce hardening reports and guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to scan agent skills, MCP configuration, tool permissions, and data surfaces they own or are authorized to inspect, then prioritize hardening work and generate guardrails for future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can place the skill into multiple agent directories, which may expose more agents than intended.

Mitigation: Install only into the specific agent directory needed for the current environment and avoid global multi-agent installation unless explicitly intended.

Risk: Scanning directories outside the user's ownership or authorization can create compliance and privacy risk.

Mitigation: Run scans only against directories and configurations the user owns or is authorized to inspect.

Risk: Scans may create local audit logs and optional report or guardrail files.

Mitigation: Account for `.yotta-hardening` audit logs and any requested report or guardrail outputs when handling sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-agent-hardening)
- [Project homepage](https://github.com/YottaMeta/yotta-agent-hardening)
- [Detection items](references/detection-items.md)
- [Guardrails template](references/guardrails-template.md)
- [Report template](references/report-template.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, and Markdown reports or guardrail files with CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan reports use class-level descriptions and avoid copyable attack payloads.]

## Skill Version(s):

0.2.6 (source: server release evidence, frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
