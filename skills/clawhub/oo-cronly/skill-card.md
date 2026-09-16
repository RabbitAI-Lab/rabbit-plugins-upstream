## Description:

Cronly helps agents operate Cronly through the OOMOL-connected oo CLI to read, create, and delete projects and job monitors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cronly action schemas and manage Cronly projects and job monitors from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions ask users to execute remote installer scripts directly in a shell without verification.

Mitigation: Review the setup path before installing and prefer a verified, pinned oo CLI installation method when available.

Risk: Cronly write and destructive actions can change or delete projects and job monitors.

Mitigation: Approve write or delete actions only after checking the exact target, payload, and expected effect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cronly)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Cronly homepage](https://cronly.app/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands, action schema inspection steps, and confirmation guidance for write or destructive Cronly actions.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
