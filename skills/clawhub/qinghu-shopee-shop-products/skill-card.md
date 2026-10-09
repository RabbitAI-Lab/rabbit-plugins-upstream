## Description:

Queries a Shopee store's popular products by shop ID and sorts them by recent sales, revenue, listing date, price, or lifetime sales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market researchers use this skill to identify popular products, competing stores' best sellers, and new listings in supported Shopee markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install or update Node/npm packages and change the host environment.

Mitigation: Review installation steps before use; run only where persistent package setup is acceptable.

Risk: Setup may configure a Qinghu API token on the machine.

Mitigation: Use a trusted qhkit environment and approve credential setup before proceeding.

Risk: Product queries can incur Qinghu credits.

Mitigation: Check the current credit estimate and obtain user consent before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shopee-shop-products)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown product list or summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on shop ID, Shopee site, billing date, sort field, and pagination; each page contains at most 10 products.]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
