## Description:

Finds a brand's top-selling Shopee products by site and daily, weekly, or monthly ranking period using Qinghu data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and analysts use this skill to identify a brand's best-selling products on a selected Shopee site and ranking period. Results can support product research and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling and an unpinned qhkit package on the host.

Mitigation: Review installation steps first and preinstall vetted tool versions rather than allowing automatic host setup.

Risk: The skill requires a Qinghu API token for product lookups.

Mitigation: Provide the token through a managed secret mechanism and avoid exposing it in commands or output.

Risk: Product lookups consume Qinghu credits.

Mitigation: Check the quoted credits and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-brand-products)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise product findings with supporting figures; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Shopee site, brand, ranking period, and date; the underlying data is not real-time.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
