## Description:

Query, install, update, and edit AI agent skills on compatible Skill Hubs, with authenticated and public workflows for search, version history, installation, card metadata edits, and team management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover, inspect, install, update, and manage skills on compatible Skill Hubs. It also supports controlled card metadata edits and team member management when the configured Hub exposes those capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote skills installed by this tool persist in an auto-loaded agent directory.

Mitigation: Install only from trusted Hubs and review downloaded skill sources before using install or update workflows.

Risk: Hub tokens may grant access to private skills or write operations.

Mitigation: Use short-lived, least-privilege tokens and avoid storing tokens in shell profiles on shared machines.

Risk: The security evidence notes that HTTPS and package authenticity are not enforced by the skill.

Mitigation: Use HTTPS-only Hub URLs and require signed packages or equivalent source review before installation.

Risk: Card metadata edits and team membership writes can change Hub state.

Mitigation: Require explicit user authorization for write workflows and rely on the skill's read, diff, verify, and rollback checks.

## Reference(s):

- [Skill Hub API Reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-hub-query)
- [skillhub.cn](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command invocations and JSON-aware CLI result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local cache data, credential-backed configuration, installed skill files, backups, and Hub metadata changes when the user authorizes the corresponding workflow.]

## Skill Version(s):

1.4.0 (source: server release evidence, artifact SKILL.md, CHANGELOG released 2026-09-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
