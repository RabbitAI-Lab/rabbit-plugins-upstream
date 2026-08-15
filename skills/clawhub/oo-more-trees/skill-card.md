## Description:

More Trees helps an agent operate a connected More Trees account by reading account, forest, project, and species data and planting or gifting trees when confirmed by the user.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to inspect a connected More Trees account, review forest statistics, list planting projects and species, and plant or gift trees through OOMOL after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The plant_trees action can change More Trees account state or consume planting credits.

Mitigation: Require explicit user confirmation of the exact payload and intended effect before running plant_trees, and use non-persistent test mode when validating inputs.

Risk: The skill can read connected More Trees account, project, balance, forest, and carbon statistics.

Mitigation: Use it only with accounts the user has connected intentionally and limit responses to information needed for the user's request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-more-trees)
- [More Trees homepage](https://www.moretrees.eco)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call the More Trees connector through the oo CLI and return JSON-shaped connector results.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
