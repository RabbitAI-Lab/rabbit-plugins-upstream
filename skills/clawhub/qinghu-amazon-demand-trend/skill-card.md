## Description:

Analyzes Amazon category demand trends using page views, product counts, return rates, and search-to-purchase ratios from Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and market analysts use this skill to assess demand trends for a selected category and marketplace before making product decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to install or upgrade Node/npm tooling and make local environment changes without clear approval.

Mitigation: Preinstall a pinned, reviewed qhkit version; require explicit approval before npm installs, npx execution, or PATH changes.

Risk: Configuring a qhkit token persists credentials in the local environment.

Mitigation: Obtain explicit approval before configuring credentials and use a securely managed token.

Risk: Demand queries consume Qinghu credits and the final cost may increase with result size.

Mitigation: Estimate credits and obtain user consent before paid calls; disclose actual credits consumed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-demand-trend)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Markdown summary with supporting metrics; spreadsheet file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports marketplace, period, sample size, and credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
