## Description:

当用户准备直播带货，需要整场流程、商品讲解、互动问答和转场话术时使用。根据排品清单、真实商品资料与已确认活动规则，输出可照读的话术和时间表。已有资料可直接写；抖音、小红书商品详情可按需补充。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External live-shopping sellers and hosts use this skill to turn product details, an item lineup, and confirmed promotion rules into a timed livestream plan, spoken product scripts, audience Q&A, transitions, and closing copy. Optional lookups can retrieve product details from Douyin or Xiaohongshu when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional product lookups send product identifiers or links to SocialDataX and may consume credits.

Mitigation: Use lookups only when product details are needed; draft from supplied information when possible, and keep the API key out of drafts and shared files.

Risk: The skill uses third-party CLI packages for optional product lookups.

Mitigation: Prefer an exact reviewed CLI version over @latest before running a lookup.

Risk: Incomplete product information can leave claims or offer terms unverified in a draft.

Mitigation: Use only supplied or retrieved product facts and confirmed promotion terms; list missing details for merchant verification before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/ecommerce-live-sales-script)
- [SocialDataX service and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with a timed livestream outline, ready-to-read product scripts, Q&A, transitions, and closing copy]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses provided product facts and confirmed offer terms; missing facts can be listed for merchant verification.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
