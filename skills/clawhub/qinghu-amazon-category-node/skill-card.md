## Description:

Queries Amazon category nodes by keyword, category name, path, or node ID and returns category hierarchies, names, and product counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and analysts use this skill to find category node IDs, inspect category paths, and assess category size across supported marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit and Node tooling in the user's environment.

Mitigation: Prefer a preinstalled, pinned qhkit version and review npm or Node installation commands before execution.

Risk: Using the tool requires a Qinghu API token and paid calls may spend credits.

Mitigation: Configure the token deliberately, check the current credit estimate, and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-category-node)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise prose with category details; a tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports category paths, names, product counts, and credits used when available; supports specified Amazon marketplaces.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
