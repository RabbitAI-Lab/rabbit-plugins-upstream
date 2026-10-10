## Description:

Queries Shopee subcategories under a selected category and site to support category exploration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to inspect child categories by site and reporting date, then drill down through category levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or upgrade local Node/qhkit tooling and configure an access token.

Mitigation: Preinstall a vetted, pinned qhkit version and configure credentials through an approved process; do not allow automatic installation or upgrades without review.

Risk: Shopee data queries can consume paid credits, including when calls fail.

Mitigation: State the expected credit cost and obtain user approval before paid calls; monitor and report actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-subcategory)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise findings with a small preview; tabular files for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should identify the Shopee site, reporting date, and sample size; paid calls report the credits consumed.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
