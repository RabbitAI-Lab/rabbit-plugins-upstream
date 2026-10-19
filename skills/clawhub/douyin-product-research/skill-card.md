## Description:

根据类目、预算和筛选条件初筛抖音商品，并给出候选清单、入选理由和待核实事项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

电商经营者和选品研究人员可按类目、预算及服务条件初筛抖音商品，比较可见信息并确定需要进一步核实的候选项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned package with an API key may expose sensitive environment variables to changed dependency code.

Mitigation: Review and pin an exact socialdatax-skills version, or run it in an isolated environment exposing only SOCIALDATAX_API_KEY.

Risk: A small sample of visible products may be mistaken for market-wide prices, sales or profitability.

Mitigation: Label the observed scope, cite returned product details and avoid sales or profit claims without supporting data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-product-research)
- [SocialDataX](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown table and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links or product IDs, visible prices, selection reasons, observation scope and follow-up checks; not a sales or profit forecast.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
