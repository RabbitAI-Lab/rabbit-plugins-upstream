## Description:

Cyberimpact lets an agent read, create, update, replace, and delete Cyberimpact groups, members, and email templates through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Cyberimpact mailing-list resources from an agent through an OOMOL-connected account, including safe read workflows and confirmed write or delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes inline remote installer commands for the OOMOL CLI.

Mitigation: Review the installer source before use and prefer a signed or version-pinned installer with checksum or signature verification.

Risk: Cyberimpact action payloads are sent through OOMOL for execution.

Mitigation: Confirm the account connection and payload contents before use, especially for customer or subscriber data.

Risk: Write and destructive actions can change or remove Cyberimpact groups, members, and templates.

Mitigation: Require user confirmation for write actions and explicit approval for destructive actions before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cyberimpact)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cyberimpact homepage](https://www.cyberimpact.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live Cyberimpact action schemas before constructing OOMOL connector payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
