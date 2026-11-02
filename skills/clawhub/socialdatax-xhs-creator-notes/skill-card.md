## Description:

用于小红书博主数据、小红书博主笔记、账号内容列表、近期发布、内容调研和创作者内容分析。覆盖 Xiaohongshu / XHS / RedNote creator notes，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Xiaohongshu creator note lists and review recent publishing, analyze content styles, benchmark creators, or track accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator IDs, profile URLs, or supplied share text are sent to SocialDataX during data requests.

Mitigation: Provide only the creator identifier or profile information needed for the request.

Risk: The CLI depends on an external npm package, and using @latest can change the installed package version.

Mitigation: Prefer an exact reviewed package version and keep SOCIALDATAX_API_KEY in the environment rather than generated files.

Risk: Unbounded pagination can increase API credit usage.

Mitigation: Set page or item limits when a bounded result set is sufficient.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-notes)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, JSON, Markdown, Shell commands]

**Output Format:** [Creator note data as JSON and concise natural-language or Markdown summaries; CLI examples as shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields vary by returned data and may include note titles or descriptions, publish times, interaction counts, media links, content types, and pagination metadata.]

## Skill Version(s):

0.1.20 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
