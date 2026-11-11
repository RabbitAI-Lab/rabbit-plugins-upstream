## Description:

Searches a user's past AI coding sessions with the deja CLI to retrieve previously settled decisions and work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to search prior AI coding sessions for decisions, previous fixes, project preferences, and relevant history before editing or recommending a change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback can download and run an unpinned package without a separate approval step, and scanner evidence is incomplete.

Mitigation: Review the fallback package and persistent rule-sync behavior before installing.

## Reference(s):

- [deja-search on ClawHub](https://clawhub.ai/vshulcz/skills/deja-search)
- [deja-vu memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise search results and decision context from prior sessions.]

## Skill Version(s):

0.24.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
