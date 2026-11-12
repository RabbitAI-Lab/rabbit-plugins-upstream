## Description:

拆解对标短剧或漫剧成片：测量集长、镜长、对白密度、开场与集尾、下一集怎么接，读出可迁移的机制，再和本项目的计划或自家成片放在同一把尺子下对照，把差距交给负责的技能补强，并用出片结果复核；需要时把一集或连续多集还原成逐字剧本、跨集统一的人物场景道具、逐镜分镜和图片与视频提示词，集与集之间接得上。用户提供对标剧的视频或字幕，说“拆解这部剧”“对标一下”“和标杆差在哪”“学学这几部爆款”“把这几集还原出来”“反推剧本和提示词”，或要拿自家成片和对标比时使用；还原结果只放在对标目录，自有或已授权的作品才能交给下游，不替创作者定节奏数值。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

短剧创作者和制作团队可用此技能测量并拆解对标短剧或漫剧，将观察结果与项目计划或自家成片按同一口径对照，再把经确认的差距交给相应创作技能处理；需要时可还原自有或已授权作品的剧本、分镜和提示词。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports unbounded memory use while processing supplied videos and says the skill does not declare its detected tool scope.

Mitigation: Review the reported memory finding and confirm the required file and shell access before installation. Use short, bounded video samples and process one clip at a time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/short-drama-breakdown)
- [拆解维度](artifact/references/breakdown-dimensions.md)
- [阶段契约](artifact/references/stage-contract.md)
- [测量与观看](artifact/references/measure-and-read.md)
- [整集与多集还原](artifact/references/reconstruct.md)
- [差距对照与出片验证](artifact/references/gap-and-learning-loop.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown reports and comparison tables, JSON measurements, and optional reconstructed script, storyboard, and prompt files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Combines measured values with qualitative observations; results depend on the supplied footage, subtitles, or transcripts.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
