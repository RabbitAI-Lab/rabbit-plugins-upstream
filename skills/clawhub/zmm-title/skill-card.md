## Description:

Generates multi-platform Chinese titles and cover text by matching the content shape to title structures, platform constraints, and red-line checks, then explains why each candidate fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing agents use this skill to produce Douyin, Xiaohongshu, WeChat, and video-account titles or cover text from a topic or draft. It returns structure labels, concise rationale, platform fit, and red-line checks so users can choose among candidates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read or write persistent vault memory for feedback and performance notes without a clear opt-in.

Mitigation: Review vault access expectations before installation and confirm or disable memory updates for workflows where persistent preference changes are not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)
- [标题结构库](references/标题结构库.md)
- [规则卡](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured title candidates, cover-text options, structure labels, rationale, and red-line notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include advice on whether a draft opening should change when the skill is called by a writing workflow.]

## Skill Version(s):

0.2.10 (source: server release metadata; artifact frontmatter lists 0.2.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
