## Description:

Listmonk helps agents manage newsletters, campaigns, mailing lists, subscribers, templates, and analytics through an OOMOL-connected Listmonk connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and marketing teams use this skill to let an agent inspect and manage Listmonk campaigns, mailing lists, subscribers, templates, previews, delivery status, and analytics through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run an unpinned remote oo CLI installer.

Mitigation: Review the installation path before installing and prefer verified OOMOL documentation or a pinned, checksum-verified release.

Risk: Write, destructive, blocklist, schedule, and send actions can modify mailing-list data or send email to subscribers.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running those actions.

## Reference(s):

- [Listmonk homepage](https://listmonk.app)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an authenticated OOMOL account, and a connected Listmonk provider before actions can run.]

## Skill Version(s):

1.0.0 (source: server evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
