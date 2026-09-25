## Description:

Manage Node-RED instances via Admin API or CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[1999azzar](https://clawhub.ai/user/1999azzar)

### License/Terms of Use:


## Use Case:

Developers and automation operators use this skill to inspect, deploy, back up, restore, and troubleshoot Node-RED flows, nodes, runtime state, and context through the Admin API or CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad live control over Node-RED flows, nodes, runtime state, and context.

Mitigation: Use it only with trusted Node-RED instances, least-privilege credentials, and manual review before deploy, delete, restore, context, or node-install actions.

Risk: Changes against production automation can disrupt running workflows.

Mitigation: Require manual change review and maintain rollback backups before using the skill on production systems.

Risk: Flow backups can contain sensitive operational data.

Mitigation: Treat generated backup files as sensitive and control their storage, access, and retention.

## Reference(s):

- [Node-RED Admin API Reference](references/admin-api.md)
- [ClawHub skill page](https://clawhub.ai/1999azzar/skills/node-red-manager)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown with inline bash commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify Node-RED flow JSON and backup files when the agent runs the provided CLI against a configured instance.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
