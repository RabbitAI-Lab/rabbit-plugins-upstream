## Description:

A Xiaohongshu content creation skill that helps creators generate notes, rewrite copy, create and score titles, design cover concepts, and check prohibited words using RedFox-backed trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, brand and e-commerce teams, and MCN/content planners use this skill to produce Xiaohongshu-ready notes, title options, cover concepts, style rewrites, and compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Features that analyze drafts, files, URLs, or public post metadata may send that data to RedFox-backed services.

Mitigation: Use only approved content, redact confidential or private material, and review generated public links and images before reuse.

Risk: The skill requires REDFOX_API_KEY for network-backed data and prohibited-word checks.

Mitigation: Store keys in environment variables, avoid hard-coding or logging them, and confirm the key source and revocation path before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-creator)
- [README.en.md](README.en.md)
- [README.md](README.md)
- [core_workflow.md](references/core_workflow.md)
- [prohibited_word_core_workflow.md](references/prohibited_word_core_workflow.md)
- [title_score_guide.md](references/title_score_guide.md)
- [xhs_hot_article_format.md](references/xhs_hot_article_format.md)
- [xhs_trend_data_format.md](references/xhs_trend_data_format.md)
- [platform-rules.md](assets/platform-rules.md)
- [RedFoxHub](https://redfox.hk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with generated copy, structured recommendations, inline command snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some features require REDFOX_API_KEY and may rely on RedFox-backed network services for trend data or prohibited-word checks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
