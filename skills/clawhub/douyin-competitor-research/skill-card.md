## Description:

当用户需要做抖音竞品研究、抖音竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向品牌、MCN、内容运营和创作者，帮助围绕关键词或选题方向检索抖音内容，并比较同赛道样本、内容角度与策略。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and source tags are sent to SocialDataX, and requests may use paid credits.

Mitigation: Avoid confidential queries and check expected credit use before searching.

Risk: The runtime API key could be exposed if handled carelessly.

Mitigation: Keep SOCIALDATAX_API_KEY private and out of prompts, logs, and shared files.

Risk: The package published under @latest can change, and a read-only skill description does not constrain the downloaded CLI's local permissions.

Mitigation: Prefer a reviewed fixed package version and check the CLI's requested permissions before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/douyin-competitor-research)
- [SocialDataX AI and API information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries with Douyin content samples and comparative observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include titles, authors or accounts, content links or IDs, available metrics and publication times, plus suggested follow-up questions.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
