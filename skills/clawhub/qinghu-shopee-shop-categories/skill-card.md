## Description:

Looks up the category distribution and sales share of a Shopee shop's popular products by shop ID.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shopee sellers and market analysts use this skill to inspect a shop's leading product categories and their sales shares for a selected site and date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may install or update external Node/npm tooling and change the local shell environment.

Mitigation: Review before installing; set up qhkit yourself where possible and avoid persistent PATH changes unless needed.

Risk: The workflow uses an API token and can incur charges for paid calls.

Mitigation: Configure QHKIT_TOKEN outside the conversation and approve paid calls only after reviewing the tools and expected cost.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-categories)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with category summaries and sales shares; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Shopee site, date and shop ID; paid calls report Qinghu credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
