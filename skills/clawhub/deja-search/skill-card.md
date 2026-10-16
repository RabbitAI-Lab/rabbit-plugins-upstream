## Description:

Helps coding agents search local AI session history for prior decisions, fixes, and workflows before starting or finishing work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to recover decisions, fixes, and commands from past local AI coding sessions before repeating work or making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic history lookup can expose sensitive information from past local AI coding sessions.

Mitigation: Use only when session-history access is appropriate and review recalled material before sharing or acting on it.

Risk: Remembered facts and synced standing rules can persist and affect other installed agents.

Mitigation: Review the exact facts or rules before saving them, and confirm the scope before syncing rules across agents.

## Reference(s):

- [Deja Search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)
- [deja-vu guide for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include references to prior sessions and recommended commands.]

## Skill Version(s):

0.22.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
