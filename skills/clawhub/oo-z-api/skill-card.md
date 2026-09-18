## Description:

Z-API helps agents inspect Z-API action schemas and operate WhatsApp messaging actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check a Z-API instance and send WhatsApp text, image, or location messages after inspecting live action schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts that execute directly in the shell.

Mitigation: Prefer an official package manager, pinned release, or downloaded installer with checksum or signature verification before installation.

Risk: Write actions can send WhatsApp text, image, or location messages to contacts or groups.

Mitigation: Confirm the exact recipient, payload, and intended effect before allowing write actions to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-z-api)
- [Z-API homepage](https://www.z-api.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from oo connector actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
