## Description:

当用户需要做百度贴吧用户需求研究、产品痛点归纳、购买顾虑整理或常见问题分析时使用。输入产品关键词、吧名或帖子链接，基于帖子与楼层讨论输出带原话依据的需求报告。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and product teams can analyze Baidu Tieba discussions to identify customer needs, use cases, pain points, purchase concerns, and FAQs. The report provides supporting post and comment excerpts and evidence scope for follow-up research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research inputs are sent to the third-party SocialDataX service.

Mitigation: Only submit research inputs you are comfortable sharing with SocialDataX.

Risk: Expanding research samples may incur API charges.

Mitigation: Start with a small sample and consider API charges before expanding it.

Risk: Installing a CLI dependency can introduce software and version risks.

Mitigation: Prefer a reviewed, fixed CLI version over @latest and limit the execution environment to the required API key and resources.

Risk: A bounded set of posts may not represent the broader Tieba user population.

Mitigation: Report sample counts and observation scope, distinguish evidence from interpretation, and do not treat mention counts as population prevalence.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/tieba-demand-insights)
- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, analysis, guidance]

**Output Format:** [Markdown research report with short source excerpts and post/comment references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports sample size, observation scope, evidence strength, and missing information; mention counts are not population estimates.]

## Skill Version(s):

0.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
