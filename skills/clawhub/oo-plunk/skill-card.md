## Description:

Plunk (useplunk.com) helps an agent read, create, update, and delete Plunk data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Plunk contact, email, event-tracking, and email-verification workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands executed directly in a shell.

Mitigation: Review the oo CLI installation path before installing; prefer a signed or package-manager install, or manually download and verify the installer.

Risk: The skill can change Plunk state, send transactional email, and delete contacts.

Mitigation: Approve write, email-sending, and delete actions only when the exact target and payload are clear; require explicit confirmation for destructive contact deletion.

## Reference(s):

- [Plunk homepage](https://www.useplunk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-plunk)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
