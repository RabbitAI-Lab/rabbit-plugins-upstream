## Description:

Typefully (typefully.com). Use this skill for ANY Typefully request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Typefully drafts, users, and social sets through an OOMOL-connected account. It supports reading Typefully data and creating, updating, or deleting drafts after confirming state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security evidence flags fallback installer commands that run remote scripts directly in a shell.

Mitigation: Review before installing, use only trusted and versioned oo CLI sources, and do not let an agent run remote installer commands automatically.

Risk: Typefully write and delete actions can change or remove account data.

Mitigation: Confirm the exact action target and JSON payload with the user before running write or destructive actions.

## Reference(s):

- [Typefully homepage](https://typefully.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Typefully ClawHub skill page](https://clawhub.ai/oomol/skills/oo-typefully)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Typefully connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
