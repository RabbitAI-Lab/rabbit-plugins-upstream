## Description:

当用户给出小红书关键词、赛道、人群或产品方向，想看热门高互动笔记样本，并拆解标题结构、内容角度、互动信号、创作灵感和选题参考时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content strategists and marketers can search public Xiaohongshu notes for a chosen topic and review sample titles, content angles, and engagement signals to inform topic research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and filters are sent to SocialDataX and may use paid credits.

Mitigation: Avoid confidential queries and use a focused topic with only the page and item limits needed.

Risk: The skill relies on an API key and an external npm package and service that were not included in the security review.

Mitigation: Store the key using the client's supported secret mechanism, never include it in prompts or skill files, and review the external dependency and service before higher-assurance use.

Risk: Returned note links retain their original query parameters, which may carry access-related information.

Mitigation: Preserve links intact when needed for note identification and share them only with the intended audience.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-viral-note-research)
- [SocialDataX product and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown research report with a sample table and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on the requested keyword and retrieved public results within the selected page and item limits; does not promise complete platform coverage or guaranteed performance.]

## Skill Version(s):

0.1.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
