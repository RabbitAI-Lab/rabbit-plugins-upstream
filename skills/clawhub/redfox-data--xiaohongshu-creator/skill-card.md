## Description:

小红书爆款内容创作专家 covers Xiaohongshu note generation, copywriting rewrites, title generation and scoring, cover design, and prohibited-word detection using RedFox trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand teams, e-commerce operators, and MCN planners use this skill to create Xiaohongshu-ready notes, rewrites, titles, cover concepts, and compliance-oriented text revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drafts, files, webpage text, and prohibited-word checks may be sent to RedFox backend services.

Mitigation: Avoid confidential or personal writing samples and use the skill only when the user is comfortable with RedFox as the backend service.

Risk: API-key discovery can read shell profile configuration if REDFOX_API_KEY is not set directly.

Mitigation: Prefer setting REDFOX_API_KEY directly in the execution environment and never hard-code or expose keys in prompts, logs, or output files.

Risk: Generated content and prohibited-word results may not fully satisfy Xiaohongshu platform review or business compliance requirements.

Mitigation: Review generated content, claims, and suggested replacements against the user's operating scope, product facts, and current platform rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/xiaohongshu-creator)
- [RedFoxHub](https://redfox.hk)
- [README.en.md](README.en.md)
- [README.md](README.md)
- [Cover Design Core Workflow](references/core_workflow.md)
- [Prohibited Word Core Workflow](references/prohibited_word_core_workflow.md)
- [Title Score Guide](references/title_score_guide.md)
- [Xiaohongshu Hot Article Data Format](references/xhs_hot_article_format.md)
- [Xiaohongshu Trend Data Format](references/xhs_trend_data_format.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown prose with titles, body copy, tags, scores, design prompts, and replacement suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to Xiaohongshu examples and compliance-oriented safe text versions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
