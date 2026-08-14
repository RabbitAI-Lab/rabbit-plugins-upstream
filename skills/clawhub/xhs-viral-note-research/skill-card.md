## Description:

当用户给出小红书关键词、赛道、人群或产品方向时，此 skill 帮助检索热门高互动笔记样本，并拆解标题结构、内容角度、互动信号、创作灵感和选题参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and content research agents use this skill to study Xiaohongshu note samples for a supplied keyword, audience, category, or product direction. It supports topic research by returning sample tables, title hooks, content angles, interaction signals, reusable ideas, and next-step recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm CLI and sends user queries using SOCIALDATAX_API_KEY.

Mitigation: Install and run it only in environments where SocialDataX and the socialdatax-skills npm package are trusted, and keep SOCIALDATAX_API_KEY scoped and protected.

Risk: Returned Xiaohongshu URLs, pagination tokens, note IDs, and recharge links may be sensitive in downstream reports.

Mitigation: Treat service-returned links and tokens as data from the provider, share reports only with intended recipients, and preserve returned identifiers without truncation or reconstruction.

Risk: Content conclusions can be misleading if interpreted as complete platform-wide coverage.

Mitigation: Frame findings as analysis of the current returned public sample set and avoid claiming deterministic traffic outcomes or exhaustive coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-viral-note-research)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research report with sample tables and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves complete Xiaohongshu note URLs, pagination tokens, and 24-character note IDs when returned; conclusions are limited to the current returned public sample set.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
