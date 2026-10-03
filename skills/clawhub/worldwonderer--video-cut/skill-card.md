## Description:

根据 Agent 选定的原片区间校验剪辑计划并拼接单个或多个视频，生成剪辑成片和质量检查结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

视频创作者和开发者用它校验已选片段的边界及必保证据，并把一个或多个源视频剪成短片；旁白由 Agent 后续单独编写。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media processing can write or replace generated files in the selected work directory.

Mitigation: Use a dedicated work directory and keep original media and backups separate from generated outputs.

## Reference(s):

- [ClawHub 视频剪辑规划 release](https://clawhub.ai/worldwonderer/skills/video-cut)
- [Shot review guidance](references/shot-review.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Video]

**Output Format:** [Shell commands, JSON validation/review reports, and MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a validated clip timeline; optional shot review reports candidates rather than automatically fixing them.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
