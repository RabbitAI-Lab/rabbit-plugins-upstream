## Description:

deja-vu memory helps an agent search the user's past AI coding sessions with the deja CLI before re-debugging errors, revisiting decisions, or re-deriving prior work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vshulcz](https://clawhub.ai/user/vshulcz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to search local AI coding-session history for prior fixes, decisions, project commands, and file rationale before repeating investigation or making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can search and reveal broad local AI-session history, which may contain sensitive past work.

Mitigation: Prefer current-project searches first, ask before cross-project or full-turn recall, and avoid surfacing secrets, credentials, personal data, or unrelated historical context.

## Reference(s):

- [deja-search ClawHub skill page](https://clawhub.ai/vshulcz/skills/deja-search)
- [deja-vu memory for OpenClaw](https://vshulcz.github.io/deja-vu/guide/memory-for-openclaw.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and summarized local-history findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local session identifiers, result status, policy-withheld counts, and superseded markers when relevant.]

## Skill Version(s):

0.21.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
