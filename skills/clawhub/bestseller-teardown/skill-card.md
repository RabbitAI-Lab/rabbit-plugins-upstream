## Description:

拆解用户已提供或已授权竞品商品页的标题、要点、图片和评论证据，整理可借鉴结构与风险；仅用于商品页静态拆解，不证明真实热销，不用于销量、库存、广告、订单或退货率结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

External Amazon sellers and operators use this skill to compare an owned ASIN with authorized competitor product pages, review evidence, and listing structure through ARI's fixed page_compare/teardown workflow. It is intended for static product-page teardown and operational decision support after quote and confirmation safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a broad ARI Amazon review and operations client, including paid, recurring, account-management, export, and local file workflows beyond a narrow one-time teardown.

Mitigation: Install and use it only when that broader ARI access is intended; review commands that use --confirm, create schedules or watches, bind competitors, export data, mark alerts or reviews, or write files locally.

Risk: Confirmed paid operations may consume credits or create recurring collection and monitoring state.

Mitigation: Run quote or capability checks first, require explicit user confirmation before --confirm, and after interrupted confirmed runs check report or status endpoints before retrying.

Risk: ARI API keys authorize account access and could be exposed through prompts, logs, screenshots, or misdirected API endpoints.

Mitigation: Store keys through the documented setup/configuration flow or ARI_API_KEY, avoid including keys in reports or command examples, and keep the custom base URL guard in place unless intentionally using a trusted development endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/bestseller-teardown)
- [ARI API reference](artifact/references/reference.md)
- [Dedicated operations workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with ARI CLI command summaries and optional exported report or review files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid operations require a quote and explicit user confirmation; reports are based on ARI-collected Amazon product-page and review samples.]

## Skill Version(s):

1.4.3 (source: SKILL.md frontmatter, artifact metadata, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
