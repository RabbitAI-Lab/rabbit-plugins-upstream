## Description:

Quaderno helps an agent read, create, update, and delete Quaderno account, contact, product, and tax-rate data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Quaderno data through an OOMOL-connected account, including reads, tax-rate calculation, and confirmed contact or product changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that execute downloaded code immediately.

Mitigation: Review the OOMOL CLI installation path first and prefer official, versioned installer documentation with checksum or signature verification.

Risk: Write actions can change Quaderno contacts or products, and destructive actions can permanently delete them.

Mitigation: Confirm the exact payload, target object, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-quaderno)
- [Quaderno homepage](https://quaderno.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Quaderno action schemas before request construction; write and delete actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
