## Description:

小红书笔记评论内容采集工具（用户洞察）。当用户需要采集/查询小红书笔记的评论内容——昵称、评论正文、点赞数、IP 属地、子评论数，提交一批笔记链接一键批量采集、导出评论明细 CSV（Excel 直开），或提到"小红书评论采集/评论内容/评论抓取/用户评论/评论导出/舆情/笔记评论"时使用本 skill。适合评论区舆情监测、用户反馈收集、爆款笔记评论洞察、KOL 粉丝声音分析等场景。**笔记链接必须带 xsec_token 参数；缺 token / xhslink 短链会自动调用转链 skill xhs-convert-url-pro 转换后提交**。收费服务（1 篇笔记 = 1 点数，注册送 10 点）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect, query, and export public Xiaohongshu note comments for sentiment monitoring, user feedback collection, creator audience analysis, and competitive note comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service endpoint uses plaintext HTTP, which can expose account tokens and exported comment data on untrusted networks.

Mitigation: Configure a valid HTTPS base URL before authenticating or running collection jobs, and avoid insecure mode unless the network and endpoint are trusted.

Risk: The skill stores an account token in a user-level configuration file and can migrate credentials from a related skill.

Mitigation: Keep the configuration file out of version control, restrict local file access, and review whether cross-skill credential migration is acceptable before use.

Risk: Collected comments can include public nicknames, comment text, and IP location, which may be personal data.

Mitigation: Use collected data only for authorized or publicly permitted analysis, minimize retention, and handle CSV exports according to applicable platform and data-compliance requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mystery77777777/skills/xhs-comments)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses on stdout, stderr progress messages, and optional CSV export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >= 18, an authenticated paid service account, and Xiaohongshu note URLs; CSV exports include public comment details such as nickname, text, like count, IP location, and reply count.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
