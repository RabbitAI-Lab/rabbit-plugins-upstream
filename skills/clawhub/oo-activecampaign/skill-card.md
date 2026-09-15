## Description:

Enables an agent to read, list, create, and update ActiveCampaign data through OOMOL's ActiveCampaign connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting users with ActiveCampaign contact management use this skill to retrieve contacts, inspect users, list fields and lists, and confirm contact upserts before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Review the installer path and prefer a versioned, signed, or package-manager source; do not run remote installer commands from an elevated shell.

Risk: The upsert_contact action can create or update ActiveCampaign contact records.

Mitigation: Confirm the exact payload and expected effect with the user before running the write action.

## Reference(s):

- [ActiveCampaign homepage](https://www.activecampaign.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-activecampaign)
- [ClawHub publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can run directly; write actions require payload and effect confirmation before execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
