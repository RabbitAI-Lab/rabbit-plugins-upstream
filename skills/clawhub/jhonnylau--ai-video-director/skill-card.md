## Description:

将剧本、小说或一句话创意转换为即梦/Seedance可用的分镜式提示词V2。支持商业广告TVC、关键歧义询问、难度分级与4-25秒自然时长判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhonnylau](https://clawhub.ai/user/jhonnylau)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video teams, and developers use this skill to turn scripts, story fragments, short creative ideas, or basic commercial ad concepts into structured Chinese storyboard prompts for AI video models. It is intended to produce usable timelines, shot descriptions, asset guidance, and clarifying questions rather than video files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill produces Chinese-formatted AI video prompts by default, which may not match all deployment language expectations.

Mitigation: Ask explicitly for another output language when a non-Chinese storyboard prompt is required.

Risk: User-provided confidential product images, unreleased creative assets, or commercial references may be passed into downstream video model workflows.

Mitigation: Avoid providing confidential or unreleased assets unless their use with the downstream video model is approved.

Risk: Complex or highly ambiguous scenes can lead to misleading storyboard assumptions if key creative choices are missing.

Mitigation: Use the skill's clarifying-question behavior for uncertain protagonists, outcomes, cultural setting, product details, or scene splitting before generating a full prompt.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jhonnylau/skills/ai-video-director)
- [README](README.md)
- [Full specification](references/full_specification.md)
- [Scoring rubric](references/scoring_rubric.md)
- [Test cases](references/test_cases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown with structured storyboard sections, shot timelines, duration guidance, asset recommendations, and negative prompt constraints.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask one to three clarifying questions before generating when key ambiguity affects the storyboard, style, result, or commercial product treatment.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
