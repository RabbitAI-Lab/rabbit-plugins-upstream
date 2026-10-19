## Description:

根据商品资料、排品清单与已确认的活动规则，生成直播带货时间表、逐商品讲解及互动转场话术，并可按需补充抖音或小红书商品详情。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

直播商家和主播根据真实商品资料及已确认的活动条件，起草可照读的直播流程、商品讲解、问答和收尾话术；商品资料不足时标明待核实事项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetching an unpinned npm package when retrieving product details means the code run later may differ from the reviewed release.

Mitigation: Pin and review the package version before execution; expose SOCIALDATAX_API_KEY only in an environment approved to run the CLI.

Risk: Unverified product claims or promotion conditions could make a live sales script misleading.

Mitigation: Confirm product facts and offer terms with the merchant; keep missing details in a separate verification list rather than the read-aloud script.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/ecommerce-live-sales-script)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Chinese-language Markdown with a timed run-of-show and read-aloud scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes product-specific claims and confirmed promotion terms, with assumptions and merchant verification items kept separate from read-aloud copy.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
