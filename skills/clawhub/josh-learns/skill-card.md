## Description:

Multi-layer memory system: fresh layer, mesh graph, auto-log, cross-layer search, compliance check, PDF vault archive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mozz0](https://clawhub.ai/user/mozz0)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use MeshMorize to give Python-capable agents persistent local memory across sessions, including daily working notes, graph-backed search, interaction logs, and PDF archival. It is suited to agent workspaces where users intentionally want durable memory and can manage storage, retention, and sync behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to preserve long-lived plaintext memory of agent interactions, which can expose sensitive, regulated, or confidential information if users log it.

Mitigation: Use it only for data you intend to retain, avoid passwords, tokens, private keys, regulated data, and confidential work, and add redaction, retention, and access controls before high-sensitivity use.

Risk: The PDF vault can sync archives to a hard-coded NAS destination when the sync script is configured and run.

Mitigation: Review, remove, or reconfigure the NAS sync script before use, and confirm the destination, SSH key, and host verification settings match the intended environment.

Risk: Documented session-dumper behavior may preserve live session content more broadly than a user expects.

Mitigation: Clarify or disable any session-dumper cron before deployment, and require explicit logging for workspaces that need tighter retention control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mozz0/skills/josh-learns)
- [Project Link Cited by Artifact Documentation](https://github.com/mozz0/MeshMorize)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; generated memory data is stored as Markdown, JSON, and PDF files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates local memory files, graph data, daily logs, and optional PDF vault archives.]

## Skill Version(s):

3.3.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
