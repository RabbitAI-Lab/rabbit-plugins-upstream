## Description:

为图片、视频和音频整理有依据的替代文本、图注、文件名建议及适用元信息，并列出字幕与章节等待补资料。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

内容编辑者、发布团队和 Agent 使用者可依据实际媒体或用户说明，为图片、视频和音频准备标注与元信息交接文件，并保留证据类型和未知项。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running another batch in the same output directory overwrites deliverables with matching names.

Mitigation: Use a separate output directory for each batch.

## Reference(s):

- [Input contract](references/input-contract.md)
- [aimeGeo GitHub](https://github.com/xxjrq/aimegeo)
- [aimeGeo documentation](https://geo.aimmme.com/docs/)
- [aimeGeo website](https://geo.aimmme.com/)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [媒体元信息 JSON 文件与图注、字幕交接 Markdown 文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按媒体逐项记录标注依据、已知信息和待补项；未知内容保持未填写。]

## Skill Version(s):

1.0.1 (source: release evidence and manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
