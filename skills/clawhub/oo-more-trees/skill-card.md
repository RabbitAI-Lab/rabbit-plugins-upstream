## Description:

More Trees helps an agent operate a connected More Trees account through OOMOL to read account, forest, project, and species data and to plant or gift trees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage a connected More Trees account from an agent, including checking account and forest status, listing planting projects, and planting or gifting trees when explicitly approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute changing code locally.

Mitigation: Prefer the official manual install guide, a package manager, or a downloaded installer with checksum or signature verification before installing the oo CLI.

Risk: The plant_trees action can change the connected More Trees account by planting or gifting trees.

Mitigation: Confirm the recipient, quantity, project, and whether test mode is enabled before approving any planting action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-more-trees)
- [More Trees Homepage](https://www.moretrees.eco)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call OOMOL connector actions that return JSON responses.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
