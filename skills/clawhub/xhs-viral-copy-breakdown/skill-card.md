## Description:

当用户给出小红书关键词、赛道、人群、产品方向、笔记链接或 note_id，想拆解爆款文案的标题钩子、开头方式、卖点表达、情绪词、内容结构、互动引导和可复用文案框架时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use the skill to analyze public Xiaohongshu posts from a keyword, topic, note link, or note ID, and identify reusable copywriting patterns such as hooks, structure, emotional language, and interaction prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and pasted links or share text are sent to SocialDataX and may consume paid credits.

Mitigation: Avoid confidential inputs and make the external service and possible credit use clear to the user.

Risk: Reports retain complete returned links, including xsec_token parameters.

Mitigation: Treat reports containing these links as sensitive and share them only when needed.

Risk: The CLI uses an API key and third-party dependencies.

Mitigation: Use a reviewed, pinned CLI version and limit access to the required credential.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-viral-copy-breakdown)
- [SocialDataX skill and API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with a sample table and structured copy analysis sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis is limited to supplied inputs and returned public samples; preserves complete returned note URLs and note IDs; does not perform account actions or promise traffic results.]

## Skill Version(s):

0.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
