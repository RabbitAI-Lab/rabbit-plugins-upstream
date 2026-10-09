## Description:

Searches a user's past AI coding sessions with the deja CLI to recover prior decisions, fixes, and working commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other AI coding assistant users search their local session history for prior decisions, fixes, commands, and recurring preferences before repeating work or changing a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searching local AI coding transcripts may surface sensitive information from past sessions.

Mitigation: Use only when the user is comfortable searching that history, and avoid sharing sensitive excerpts unnecessarily.

Risk: Persistent memory or rules synchronization may save or propagate a rule beyond the current session.

Mitigation: Use remember or rules sync only with the user's explicit intent and review the exact text before saving or syncing.

## Reference(s):

- [deja-vu memory for OpenClaw guide](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)
- [deja-search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with session references and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are limited to indexed local sessions; a missing or partial result is not proof that a past decision does not exist.]

## Skill Version(s):

0.21.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
