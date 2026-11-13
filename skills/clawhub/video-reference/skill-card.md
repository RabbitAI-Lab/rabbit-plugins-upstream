## Description:

按需分析一部已完成的解说成片，提炼镜头节奏、响度、段落与音轨分工，并导出可复用的制作参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

供视频编辑与制作人员按需拆解已完成的解说成片，查看实测节奏与声音指标，并把可迁移的制作方法整理为下一次制作可用的参考。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An export may lack enough source-matched transcript and entity evidence to verify that names or dialogue were excluded; the security scan was partial.

Mitigation: Export only when source-matched transcript and entity evidence is available, review the exported JSON for names and dialogue, and check that the host restricts file and shell access.

## Reference(s):

- [ClawHub release](https://clawhub.ai/worldwonderer/skills/video-reference)
- [reference-schema.md](artifact/references/reference-schema.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Files]

**Output Format:** [JSON production reference with measured video and audio metrics, reusable methods, and local review images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local workflow; the exported production_reference.json is designed to omit source names and dialogue.]

## Skill Version(s):

1.0.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
