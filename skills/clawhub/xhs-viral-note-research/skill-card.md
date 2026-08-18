## Description:

当用户给出小红书关键词、赛道、人群或产品方向，想看热门高互动笔记样本，并拆解标题结构、内容角度、互动信号、创作灵感和选题参考时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content marketing teams use this skill to research public Xiaohongshu search results for a keyword, audience, product direction, or topic niche. It helps compare high-engagement note samples, title hooks, content angles, interaction signals, reusable topic ideas, and next-step research suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key and sends XHS research keywords to the SocialDataX service.

Mitigation: Use it only when the user is comfortable providing that API key and sharing the requested research keywords with SocialDataX.

Risk: Reports may include full XHS URLs with xsec_token parameters because the skill preserves raw source links for attribution.

Mitigation: Review outputs before sharing or storing them where full source URLs or query parameters are not appropriate.

Risk: The returned samples cover only the requested keywords and page range and may not represent the full platform.

Mitigation: Present findings as sample-based research and avoid claiming complete coverage or guaranteed traffic outcomes.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/xhs-viral-note-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research report with a sample table, concise analysis, and optional command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves returned XHS URLs and note IDs for attribution; conclusions are limited to the requested keywords and returned page range.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
