## Description:

Estimates an indoor plant transpiration-rate index from thermal or RGB leaf images plus optional environmental data, producing water-stress, root water-uptake, and plant-care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, plant-care teams, greenhouse operators, and smart-planter workflows use this skill to analyze leaf images or videos, estimate a relative transpiration-rate index, assess root water-uptake vitality, and retrieve cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs may be sent to Life Emergence cloud APIs for analysis.

Mitigation: Use only approved media, disclose cloud processing to users, and avoid submitting sensitive or unnecessary visual data.

Risk: Cloud report history is tied to an internally created or reused identity.

Mitigation: Constrain identity-related environment variables and confirm that report-history behavior matches the deployment's consent and retention expectations.

Risk: Tokens and user records may be stored in a local workspace SQLite database.

Mitigation: Limit workspace file access, protect or rotate stored credentials, and remove local state when the skill is decommissioned.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and tables, with optional JSON/detail output and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save output to a caller-specified file; historical report queries return structured report records with links when available.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
