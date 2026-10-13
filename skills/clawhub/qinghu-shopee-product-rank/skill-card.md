## Description:

Queries Shopee category-level best-selling and rising-product rankings by site and day, week, or month, with cross-border, local, and shop-type filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and market researchers use this skill to identify popular or fast-growing Shopee products within a chosen category, market, and ranking period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill proposes installing or upgrading external Node tooling and may change the shell PATH.

Mitigation: Use a preinstalled, pinned qhkit version and require approval before package installation or PATH changes; avoid npx and latest-version setup during routine use.

Risk: Using the service requires a Qinghu API token that the skill may persist locally.

Mitigation: Require approval before supplying or storing a token and keep it out of shared logs and outputs.

Risk: Ranking queries can incur paid Qinghu credits.

Mitigation: Show the estimated cost and obtain explicit approval before each authorized set of paid calls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shopee-product-rank)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise ranking summary with key product previews and an optional table file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the site, period, and sample size; paid calls report credits consumed.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
