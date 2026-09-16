## Description:

用 Cue 穿透待核查资讯的表层表述，通过独立信源交叉验证与底层数据复核，识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to fact-check claims, news, research excerpts, diligence material, and market rumors with Cue. It produces structured reports that compare the submitted text against correction evidence, independent sources, timelines, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted material is transmitted to Cue and may be processed with external sources.

Mitigation: Use only after confirming the user is comfortable with that transfer, and redact confidential, personal, or legally sensitive content before submission.

Risk: The skill includes invitation, credit, discount, and payment guidance that can read as promotional.

Mitigation: Present those items only as Cue platform options and not as independent financial or operational advice.

Risk: The server security verdict is suspicious.

Mitigation: Review the skill before installation and scan it again before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner repository referenced by artifact](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Structured Markdown fact-check report with source links and operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Cue API access; final reports should include the Cue share link when an actual conversation ID is available.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata; artifact frontmatter declares 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
