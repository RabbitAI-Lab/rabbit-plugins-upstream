## Description:

拆解用户已提供或已授权竞品商品页的标题、要点、图片和评论证据，整理可借鉴结构与风险；仅用于商品页静态拆解，不证明真实热销或销量。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to compare a main ASIN with authorized competitor pages, then receive a static teardown of page structure, review evidence, reusable patterns, and risks. It is intended for listing analysis and operations planning, not for sales, inventory, advertising, order, or return-rate conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ARI API key can allow access to ARI account data, saved reports, review data, monitoring state, and credit-consuming analysis workflows.

Mitigation: Use the browser authorization flow or local configuration only, do not share the API key in chat, and install the skill only for accounts where this access is acceptable.

Risk: Some workflows can consume ARI credits, and account autoconfirm settings may allow small or previously authorized paid actions to run without a fresh prompt.

Mitigation: Use explicit wording such as 'only quote, do not execute' when checking price, review autoconfirm settings, and require clear confirmation before paid operations when confirmation is requested.

Risk: Static page and review teardown can be mistaken for proof of true bestseller status, sales volume, inventory, advertising performance, orders, or return rates.

Mitigation: Treat outputs as listing and review evidence only, and validate business conclusions with separate authoritative sales, inventory, advertising, order, or returns data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/bestseller-teardown)
- [Amazon 热销商品页拆解 README](artifact/README.md)
- [专属运营工作流](artifact/references/operation-workflow.md)
- [ARI CLI 与 API 参考](artifact/references/reference.md)
- [ARI 用户中心](https://ari.funewa.com/zh/account)
- [ARI 报告中心](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis and concise natural-language guidance, with shell commands only for authorization or advanced operation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ARI report links, account and credit status, data-window caveats, and cost confirmations when applicable.]

## Skill Version(s):

1.4.8 (source: evidence.release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
