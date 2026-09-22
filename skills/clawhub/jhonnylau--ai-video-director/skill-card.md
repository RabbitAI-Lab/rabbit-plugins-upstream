## Description:

将剧本、小说或一句话创意转换为即梦/Seedance可用的分镜式提示词V2。支持商业广告TVC、关键歧义询问、难度分级与4-25秒自然时长判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhonnylau](https://clawhub.ai/user/jhonnylau)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and video prompt writers use this skill to turn scripts, story excerpts, outlines, or single creative ideas into structured Chinese storyboard prompts for AI video models such as Jimeng and Seedance. It helps plan mode, complexity, duration, assets, dialogue, and shot-by-shot prompt structure for short video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may recommend uploading product, character, scene, or other reference assets to external video or model platforms.

Mitigation: Only provide assets that are approved for sharing with the target external platform and review platform terms before upload.

Risk: Generated storyboard guidance can be unsuitable when the source request has unresolved critical ambiguity or asks for extremely complex scenes.

Mitigation: Use the skill's clarification questions, complexity warnings, segmentation guidance, and manual review before using prompts in production video workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jhonnylau/skills/ai-video-director)
- [Publisher profile](https://clawhub.ai/user/jhonnylau)
- [Full specification](artifact/references/full_specification.md)
- [Scoring rubric](artifact/references/scoring_rubric.md)
- [Test cases](artifact/references/test_cases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese Markdown with structured storyboard prompt sections and time-coded shot breakdowns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include mode selection, AI implementation difficulty, suggested duration, asset guidance, optional segmentation or clarification questions, and V2 storyboard prompts.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
