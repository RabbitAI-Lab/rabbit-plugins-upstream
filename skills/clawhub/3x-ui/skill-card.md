## Description:

Interacts with the 3x-ui panel REST API to manage Xray proxy panel configuration, clients, nodes, server status, subscriptions, and backups using bearer tokens or session cookies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to generate API calls, command examples, and workflow guidance for administering 3x-ui/Xray panels. It supports client lifecycle, traffic, node, subscription, backup, and server status tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers powerful panel operations, including delete, reset, restart, import, update, backup, and credential-management endpoints.

Mitigation: Require explicit confirmation and current backups before using destructive or service-changing endpoints, especially on production or shared panels.

Risk: Example scripts accept live panel tokens as command-line arguments, which can expose credentials through shell history, process listings, chat logs, or terminal logs.

Mitigation: Use least-privilege, revocable API tokens and avoid pasting live tokens into command lines or chat transcripts; prefer safer secret-passing mechanisms when adapting the scripts.

Risk: The security verdict is suspicious because the skill is coherent but lacks enough guardrails around privileged administration actions.

Mitigation: Review the skill before installation and restrict use to trusted operators with appropriate access to the target 3x-ui panel.

## Reference(s):

- [3x-ui API Complete Reference](references/api_reference.md)
- [ClawHub Skill Page](https://clawhub.ai/lanlan314/skills/3x-ui)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands, REST endpoint paths, and JSON request or response shapes for 3x-ui panel APIs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
