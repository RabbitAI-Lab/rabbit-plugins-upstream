## Description:

Visible OpenClaw-Open WebUI council rooms with typed blackboards and session handovers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to coordinate visible multi-model council sessions between OpenClaw and Open WebUI, preserving typed blackboard entries, handovers, decisions, evidence, and unresolved questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write Open WebUI chat records and keep council boards on disk.

Mitigation: Review the configured Open WebUI database path and retention expectations before use; prefer a dedicated local account or test WebUI profile until cleanup expectations are clear.

Risk: The skill can launch and stop background OpenClaw sessions through local service commands.

Mitigation: Review executable override environment variables and run the integration only where the local OpenClaw and Open WebUI permissions are intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pinguy/skills/council-blackboard)
- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/council-blackboard)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local council board records and returns Open WebUI chat URLs, board paths, route IDs, handover text, and status JSON.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
