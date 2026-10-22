## Description:

Searches local AI coding-session history with deja-vu to recover past decisions, fixes, and project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to find prior decisions, working commands, and related fixes before making or reviewing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frequent searches can expose sensitive material from local AI coding transcripts to the agent.

Mitigation: Install only if local transcript access is acceptable, and review recalled content before relying on it.

Risk: Past transcript instructions or synced rules may incorrectly influence current or global agent behavior.

Mitigation: Treat recalled material as untrusted context and approve remembered or synced rules before they change global behavior.

## Reference(s):

- [deja-search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)
- [deja-vu memory guide for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results draw from local AI coding-session history and may need confirmation before use.]

## Skill Version(s):

0.22.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
