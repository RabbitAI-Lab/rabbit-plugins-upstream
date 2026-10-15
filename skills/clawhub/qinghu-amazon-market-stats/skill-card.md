## Description:

Analyzes an identified Amazon category's market size, maturity, leading-product concentration, new-product prospects, and price and sales differences using Qinghu market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and market researchers use this skill to evaluate whether an identified category is worth entering, how concentrated its leading listings are, and whether new products can gain traction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node or changing PATH modifies the host environment.

Mitigation: Review installation and environment changes first; prefer a preinstalled, pinned qhkit version in a controlled environment.

Risk: Qinghu API tokens may be stored or passed to a command, and market-data calls may consume paid credits.

Mitigation: Handle tokens securely and approve paid calls only after checking the credit estimate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-stats)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Spreadsheet files]

**Output Format:** [Concise narrative with supporting figures and an optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures identify the Amazon marketplace, time period, and sample size; paid calls report Qinghu credits used.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
