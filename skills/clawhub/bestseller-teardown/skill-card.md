## Description:

拆解用户已提供或已授权竞品 Amazon 商品页的标题、要点、图片和评论证据，整理可借鉴结构与风险。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare an authorized main ASIN with competitor product pages, quote the ARI operation, and generate a structured page teardown after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks for broader ARI account, monitoring, export, and paid-operation authority than the narrow product-page teardown description suggests.

Mitigation: Install only when the user trusts the ARI service and wants these broader operations; review the skill before use.

Risk: The skill can spend ARI credits under confirmation or auto-confirm rules.

Mitigation: Disable or lower auto-confirm rules when each paid action should require explicit approval.

Risk: The skill can export reports or reviews to local files.

Mitigation: Treat exported files as potentially sensitive business data and store or share them according to the user's data-handling policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bestseller-teardown)
- [ARI CLI and API reference](artifact/references/reference.md)
- [Dedicated page teardown workflow](artifact/references/operation-workflow.md)
- [ARI product management](https://ari.funewa.com/zh/products)
- [ARI reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown report with supporting CLI command guidance and ARI report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and may create local exports or saved ARI reports depending on user-confirmed actions.]

## Skill Version(s):

1.4.5 (source: server release evidence, SKILL.md frontmatter, _meta.json, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
