## Description:

Retrieves reviews for an Amazon ASIN by star rating and review type, including titles, content, ratings, and dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to examine customer feedback and identify complaints for a specific Amazon product and marketplace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade unpinned Node and qhkit tooling or persist shell PATH changes.

Mitigation: Preinstall a reviewed, pinned qhkit version and require explicit approval before npm, npx, PATH, or shell-profile changes.

Risk: Review queries require a Qinghu API token and may incur usage charges.

Mitigation: Provide the token securely, check the current price, and obtain consent before paid queries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-review)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise review summary with optional table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, sample size, and credits charged; larger result sets can be exported to a table file.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
