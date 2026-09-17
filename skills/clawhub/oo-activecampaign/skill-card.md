## Description:

Operate ActiveCampaign through the OOMOL oo CLI to read, create, and update contacts, user data, custom fields, and mailing lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate an ActiveCampaign account through an OOMOL-connected account, including contact lookup, contact listing, field and list discovery, current-user lookup, and confirmed contact upsert workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Review the OOMOL CLI installation method before installing and prefer official package-manager or verified download steps.

Risk: The upsert_contact action can change ActiveCampaign contact data.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ActiveCampaign homepage](https://www.activecampaign.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-activecampaign)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schema and run commands; read actions can run directly, while write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
