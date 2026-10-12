## Description:

Queries up to 720 days of Shopee product trends aggregated by month, quarter, or year through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and product analysts use this skill to assess a product's longer-term sales trajectory and lifecycle across monthly, quarterly, or yearly periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update Node/npm software and change the host PATH.

Mitigation: Require approval before installation, use a managed environment, and prefer pinned package versions.

Risk: Qinghu API credentials may be stored on the host.

Mitigation: Use managed secrets and review where credentials are stored before configuring qhkit.

Risk: Trend queries may consume paid Qinghu credits.

Mitigation: Estimate costs and obtain explicit user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-product-trend)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Shell commands]

**Output Format:** [Concise text or Markdown analysis; tabular files for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the site, period, sample size, and credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
