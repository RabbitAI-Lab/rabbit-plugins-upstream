## Description:

Personal Understanding v2 gives an AI agent a local, verbatim-first personal memory archive with timeline, entity, follow-up, retrieval, and audit workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caix84476-netizen](https://clawhub.ai/user/caix84476-netizen)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an AI agent capture personal material verbatim, retrieve it through auditable context, and maintain follow-ups without relying on lossy summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a durable local archive of sensitive personal conversations and files.

Mitigation: Install only when that archive is intentional, and confirm how to inspect or delete data under `memory/`, `sources/`, and `backups/` before use.

Risk: The installer can modify AI-client configuration through MCP auto-registration.

Mitigation: Review the registration behavior and resulting client configuration before relying on the installed MCP tools.

Risk: Optional backups can mirror private archive data to a cloud or rclone destination.

Mitigation: Disable or avoid cloud and rclone backups unless the destination was deliberately configured and approved by the user.

Risk: Retrieval traces and turn receipts may preserve sensitive context about user conversations.

Mitigation: Decide whether those audit records are acceptable for the deployment before enabling routine use.

## Reference(s):

- [Server-resolved source repository](https://github.com/caix84476-netizen/personal-understanding)
- [ClawHub skill page](https://clawhub.ai/caix84476-netizen/skills/personal-understanding)
- [PyPI package](https://pypi.org/project/personal-understanding/)
- [Architecture v2](references/architecture-v2.md)
- [Capture and verbatim policy](references/capture-and-verbatim-policy.md)
- [Retrieval policy](references/retrieval-policy.md)
- [Maintenance and durability](references/maintenance-and-durability.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and agent responses with inline shell commands or structured local-script output when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist sensitive personal content and local archive state when the agent uses the skill.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact version 2.2.0 in SKILL.md, VERSION, pyproject.toml, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
