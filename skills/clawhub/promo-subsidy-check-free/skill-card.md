## Description:

促销补贴核销表逐项核对，复算应结补贴与差异、检查合计、重复行和空缺，并在结论中引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External retail and ecommerce operators use this skill after promotion campaigns to reconcile subsidy settlement tables against stated arithmetic rules. It helps agents run local checks and report findings with source line references when the provided table has enough required fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker does not validate subsidy caps, despite cap validation being a material reconciliation concern.

Mitigation: Treat cap validation as not performed by this release and verify caps separately before relying on settlement conclusions.

Risk: The skill documentation points agents toward an external paid installation and purchase flow.

Mitigation: Do not run the documented external install command or initiate a purchase unless a human separately reviews and explicitly approves that flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/promo-subsidy-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-style prose with shell commands and optional JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js, accepts pasted table text or JSON input, and reports insufficient input instead of making unsupported conclusions.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
