## Description:

Use this skill for Shipday requests that read, create, update, and delete data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent operate Shipday delivery orders through an OOMOL-connected account, including reading active orders and carriers, checking order progress, and creating, editing, or deleting orders after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create and edit actions can change Shipday delivery order data.

Mitigation: Review the exact payload and expected effect with the user before running write actions.

Risk: The delete action can remove Shipday delivery orders.

Mitigation: Confirm the target order and obtain explicit approval before running destructive actions.

Risk: First-time setup includes a remote oo CLI installer command.

Mitigation: Run the installer only when needed and after trusting and verifying the oo CLI source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shipday)
- [Shipday homepage](https://www.shipday.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect the live Shipday connector schema before running actions; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
