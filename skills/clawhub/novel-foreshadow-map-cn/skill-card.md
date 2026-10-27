## Description:

输入单次章节、场景摘要或短段落，梳理其中可验证的伏笔、首次埋点、已兑现与待兑现状态，并给出建议回收位置表。适用于修订前连续性核查与伏笔追踪；材料不足时明确列出缺项，不臆测整本剧情。单次最多处理100行，超量须分批提供。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

小说作者和编辑可用它对章节摘要、场景梗概或短段落进行连续性核查，整理有证据的伏笔、首次埋点、兑现状态和建议回收位置。材料不足时，它会列出缺项并将无法判断的线索标为待确认。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented installer command does not pin a version or source revision.

Mitigation: Review the installer version and source revision before installation, and pin both where possible.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/xxjrq/skills/novel-foreshadow-map-cn)
- [Story Skills repository (business-purpose reference)](https://github.com/danjdewhurst/story-skills)
- [Revision Continuity Skill (business-purpose reference)](https://github.com/danjdewhurst/story-skills/blob/main/skills/revision-continuity/SKILL.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown table with a coverage summary, missing-context notes, and optional prioritized recovery suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tracks up to 100 rows per batch; larger inputs should be split by chapter or scene.]

## Skill Version(s):

1.0.0 (source: release evidence, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
