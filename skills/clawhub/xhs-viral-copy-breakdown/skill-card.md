## Description:

当用户提供小红书关键词、赛道、人群、产品方向或笔记链接时，拆解高互动文案并提炼可复用的表达框架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

小红书创作者和社媒研究人员可用它分析关键词搜索结果或指定笔记的标题钩子、内容结构、情绪表达和互动引导，并整理成可复用的文案框架。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and note links are sent to SocialDataX for research.

Mitigation: Use only search terms and links you are comfortable sharing with SocialDataX, and review complete returned URLs before sharing them.

Risk: The skill uses an externally distributed CLI package whose behavior may change between releases.

Mitigation: Keep the API key in supported secret storage and prefer a reviewed, pinned CLI version. The security review covers the supplied skill instructions, not the external package or future releases.

## Reference(s):

- [SocialDataX service and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-viral-copy-breakdown)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with a sample table, copy analysis, and reusable writing frameworks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on the supplied query or selected public samples; unavailable fields are identified rather than inferred.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
