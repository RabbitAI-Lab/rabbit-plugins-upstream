## Description:

ClickHelp (clickhelp.com). Use this skill for reading, creating, and updating ClickHelp data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect ClickHelp schemas, search and retrieve ClickHelp projects and topics, and create or update ClickHelp topic content through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions reference unverified remote installer scripts.

Mitigation: Review the setup path before installing; prefer a pinned, verified oo CLI release or a trusted package manager.

Risk: Topic creation and update actions can change ClickHelp content.

Mitigation: Confirm exact payloads and expected effects with the user before running create_topic or update_topic.

Risk: Connector actions use the scopes available through the OOMOL-connected ClickHelp account.

Mitigation: Connect only ClickHelp scopes the user is comfortable allowing OOMOL-backed connector actions to use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-clickhelp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClickHelp Homepage](https://clickhelp.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
