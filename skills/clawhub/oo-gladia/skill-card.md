## Description:

Gladia helps agents operate Gladia pre-recorded transcription workflows through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to start, inspect, list, retrieve, download, and delete Gladia pre-recorded transcription jobs from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can execute a mutable remote installer with the user's privileges.

Mitigation: Install only after reviewing the official installer or using a pinned, verifiable package from a trusted OOMOL CLI distribution path.

Risk: Write and destructive Gladia actions can change or delete account data.

Mitigation: Confirm the exact payload, target, and effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gladia)
- [Gladia homepage](https://app.gladia.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke OOMOL oo CLI commands that return JSON responses from Gladia connector actions.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
