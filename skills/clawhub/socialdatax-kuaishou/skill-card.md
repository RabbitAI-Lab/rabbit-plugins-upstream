## Description:

用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can research Kuaishou / Kwai content and creators by searching videos and accounts, reviewing individual works and comments, and retrieving creator profiles and posted works.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, links or share text, and identifiers supplied for research are processed by SocialDataX.

Mitigation: Submit only information needed for the requested lookup and omit unrelated private details.

Risk: The API key could be exposed through chat, logs, or version control.

Mitigation: Keep SOCIALDATAX_API_KEY in a protected secret store and never paste the key into chat or commit it.

Risk: Unpinned CLI dependencies and broad retrieval requests can introduce dependency or paid-usage risk.

Mitigation: Use a reviewed fixed CLI version and set page and item limits for retrievals.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured SocialDataX Kuaishou data with optional concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; available records and volume depend on API access and retrieval limits.]

## Skill Version(s):

0.1.22 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
