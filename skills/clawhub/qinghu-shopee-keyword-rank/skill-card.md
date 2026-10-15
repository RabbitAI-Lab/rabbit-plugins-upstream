## Description:

Helps agents retrieve Shopee category keyword rankings by site, date, and daily, weekly, or monthly period, including best-selling and rising terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to compare popular or fast-rising Shopee search terms within a category, marketplace, and reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit can change local Node/npm tooling and persist shell configuration.

Mitigation: Review the exact package and version first; prefer a disposable or managed environment and avoid shell startup edits unless intended.

Risk: The skill handles a qhkit token and paid Qinghu API calls, which may consume credits.

Mitigation: Keep the token protected, check the current credit estimate, and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-keyword-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Brief findings and preview in Markdown; table file for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes marketplace and period context and reports Qinghu credits consumed for paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
