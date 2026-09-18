## Description:

More Trees lets an agent operate a connected More Trees account through the OOMOL oo CLI to read account, forest, project, and planting information and plant or gift trees after confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a user's connected More Trees account: checking account and forest details, listing planting projects and species, and planting or gifting trees after explicit confirmation for live write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The plant_trees action can change the connected More Trees account by planting or gifting trees.

Mitigation: Require explicit user confirmation of live or test mode, project, species, quantity, recipient, and cost before running the action.

Risk: The first-time setup text includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Prefer a verifiable package, pinned installer, or reviewed installation process before executing installer commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-more-trees)
- [More Trees Homepage](https://www.moretrees.eco)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and may include connector JSON results or confirmation prompts for write actions.]

## Skill Version(s):

1.0.2 (source: server evidence release.version and artifact frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
