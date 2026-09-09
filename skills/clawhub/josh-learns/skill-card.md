## Description:

Memory system for AI agents on OpenClaw-like hosts. File-based multi-layer memory: fresh daily layer (5-day rotation), mesh graph, auto-log of every exchange, cross-layer grep search, compliance check, crash-gap recovery from session transcripts, automation-registry lookup. Search before answering, log after answering. Local-first, $0 to run, survives restarts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mozz0](https://clawhub.ai/user/mozz0)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to give OpenClaw-like agents persistent local memory across sessions. It supports searching prior context, logging meaningful exchanges, maintaining a lightweight memory graph, checking memory health, and recovering gaps from local transcript records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently records agent conversations as searchable plaintext local memory.

Mitigation: Install only for users who explicitly want persistent local memory; avoid logging secrets, redact sensitive content, and keep memory directories out of public repositories.

Risk: Transcript recovery and automation-registry lookup can expose privileged local conversation or reminder data.

Mitigation: Require explicit user approval before using those workflows, use a private temporary directory, avoid verbatim replay by default, redact secrets, and delete copied databases immediately.

Risk: The security guidance flags memcheck for shell=True and untrusted PATH execution.

Mitigation: Fix memcheck to avoid shell=True and resolve trusted command paths before deploying it in a shared or sensitive environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mozz0/skills/josh-learns)
- [README.md](README.md)
- [SKILL.md](SKILL.md)
- [LICENSE](LICENSE)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with inline shell commands and Python utilities that create or update local Markdown and JSON memory files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces local filesystem changes under the configured agent workspace, including daily logs, fresh context files, checkpoints, decision records, and a mesh graph.]

## Skill Version(s):

4.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
