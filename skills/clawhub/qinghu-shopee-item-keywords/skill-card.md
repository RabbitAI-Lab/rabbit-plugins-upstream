## Description:

Analyzes Shopee product search-traffic keywords and recommends popular keywords in the same category using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and analysts use this skill to identify the search terms bringing traffic to specified products and discover popular terms in the same category across supported Shopee sites.

### Deployment Geography for Use:

Global; queries cover the supported Shopee sites in Taiwan, Malaysia, Indonesia, Thailand, the Philippines, Singapore, Vietnam, and Brazil.

## Known Risks and Mitigations:

Risk: Installing qhkit or other dependencies without review can introduce untrusted software.

Mitigation: Review the package before installation and prefer preinstalled, vetted dependencies.

Risk: Persistent API tokens may expose Qinghu account credentials.

Mitigation: Use a scoped QHKIT_TOKEN environment variable where possible rather than storing a persistent token.

Risk: Qinghu data queries can incur paid credits.

Mitigation: Check the current estimate and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-item-keywords)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files]

**Output Format:** [Concise text or Markdown summary; tabular file for ten or more results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports site, period, sample size, and Qinghu credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
