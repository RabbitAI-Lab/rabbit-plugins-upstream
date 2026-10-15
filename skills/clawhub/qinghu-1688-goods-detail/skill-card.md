## Description:

Retrieves 1688 product details by offer ID, including title, price, sales, and seller information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and sourcing teams use this skill to look up a 1688 offer by product ID or link and review its price, sales, and seller details before purchasing or comparing suppliers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime setup can install unpinned external packages and change the user's environment.

Mitigation: Prefer a preinstalled, pinned qhkit version and require explicit approval before installing packages or changing PATH.

Risk: Token configuration and paid API calls can expose credentials or incur charges.

Mitigation: Request approval before token setup or paid calls; disclose estimated credits before calling.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-1688-goods-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise product-detail summary; optional table file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits spent after paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
