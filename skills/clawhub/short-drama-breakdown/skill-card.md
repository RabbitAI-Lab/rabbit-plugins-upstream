## Description:

拆解对标短剧或漫剧成片，测量结构与节奏、提炼可迁移机制并和本项目对照；需要时还原一集或连续多集供分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者与开发团队使用此技能分析用户提供或授权的对标短剧，将可复核的测量结果与项目计划或自有成片对照，形成差距报告；按登记的允许用途，在需要时还原剧集供分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Large videos may exhaust memory because processing resource limits are not enforced.

Mitigation: Process short episodes at default sampling rates and limit each run to the selected episodes.

Risk: Uploading reference footage to an external model service can expose material and incur quota or billing costs; provider data handling was not independently verified in the static review.

Mitigation: Upload only when the reference registration permits it, and approve the named service and its quota or billing implications first. Otherwise use local measurement.

Risk: Reconstructed dialogue, identities, or shot details may be inaccurate.

Mitigation: Check reconstructions against the source video, subtitles, and measured cuts, and mark details without direct support as inferred.

## Reference(s):

- [测量与观看](references/measure-and-read.md)
- [拆解维度](references/breakdown-dimensions.md)
- [整集与多集还原](references/reconstruct.md)
- [差距对照与出片验证](references/gap-and-learning-loop.md)
- [拆解学习阶段契约](references/stage-contract.md)
- [ClawHub 技能发布页](https://clawhub.ai/worldwonderer/skills/short-drama-breakdown)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Text, Shell commands]

**Output Format:** [Markdown reports, structured JSON measurements, and text artifacts such as scripts, storyboards, and prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Measurement outputs include episode timing, shot data, and sampled frame sheets; findings distinguish observation, interpretation, and unknowns.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
