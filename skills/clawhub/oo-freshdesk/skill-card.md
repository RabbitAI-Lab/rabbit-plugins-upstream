## Description:

Freshdesk helps agents inspect Freshdesk account details, tickets, ticket lists, and ticket conversations through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and developer agents use this skill to read Freshdesk account and ticket information from a connected OOMOL account. It is suited for searching tickets, inspecting ticket details, and reviewing ticket conversations before taking any separate support action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include a remote shell or PowerShell installer for the oo CLI.

Mitigation: Review the oo CLI installation path before installing, prefer a signed or checksum-verified installer when available, and run setup with ordinary user privileges.

Risk: The skill reads Freshdesk account, ticket, and conversation data that may include support or customer information.

Mitigation: Use an appropriately scoped connected account and treat this release as read-oriented unless a future version explicitly documents and scopes write actions.

## Reference(s):

- [ClawHub Freshdesk skill page](https://clawhub.ai/oomol/skills/oo-freshdesk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Freshdesk homepage](https://www.freshworks.com/freshdesk/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from executed connector actions are JSON objects with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
