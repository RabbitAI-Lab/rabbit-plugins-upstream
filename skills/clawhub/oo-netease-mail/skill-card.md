## Description:

Operate NetEase Mail through OOMOL's netease_mail connector for reading, sending, replying, forwarding, moving, marking, deleting, and downloading mail data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate a connected NetEase Mail account through the OOMOL oo CLI, including read workflows, message composition, attachment downloads, and mailbox management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow can execute remote installer scripts for the oo CLI.

Mitigation: Use a verified, versioned installer source with checksums or signatures before running installation commands locally.

Risk: Write and destructive actions can alter or delete NetEase Mail messages.

Mitigation: Confirm the exact mailbox target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-netease-mail)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [NetEase Mail](https://mail.163.com/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command responses are JSON when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
