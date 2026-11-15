## Description:

当用户需要做今日头条内容研究、文章选题、热点角度整理或同主题内容对比时使用。输入主题或内容链接，基于相关作品和详情输出样本概览、标题模式与可继续验证的内容方向。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部内容创作者和研究人员可用它查看今日头条热榜、搜索相关作品并读取代表内容详情，以整理标题模式、内容角度和后续选题方向。分析应基于返回样本，并说明样本范围与缺失信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill suspicious with medium confidence because it runs a changeable CLI package that could access credentials or other data; the scan was partial.

Mitigation: Review the CLI package and version before use, and make credentials available only in an execution environment you trust.

Risk: Research topics and links may be sent to SocialDataX.

Mitigation: Consider whether the topic or link is appropriate to submit to the service before running a search or detail lookup.

## Reference(s):

- [ClawHub release](https://clawhub.ai/devinchen2014/skills/toutiao-content-research)
- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown research summary with sample links or content IDs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes returned hot-search or keyword samples and selected content details; identifies observation time, sample scope, and missing information where available.]

## Skill Version(s):

0.1.5 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
