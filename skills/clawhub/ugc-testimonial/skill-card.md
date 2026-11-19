## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

电商营销人员可用它为商品和目标人群撰写口播脚本、设计分镜，并生成 UGC 风格的商品种草视频。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to external generation providers, and the security scan reports incomplete coverage.

Mitigation: Before generation, check whether sharing prompts and images with the selected provider suits your privacy needs.

Risk: Synthetic UGC may be mistaken for a real buyer testimonial.

Mitigation: Do not present fictional experiences as real reviews, and label AI-generated content as required by the target platform.

## Reference(s):

- [Video backend configuration](references/video-backends.md)
- [Provider CLI reference](references/provider-cli.md)
- [Brand kit reference](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Video, Subtitle files, Shell commands]

**Output Format:** [口播脚本与分镜文本、JSON 分镜文件、生成的视频片段或成片，以及可选 SRT 字幕]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video does not provide reliable lip synchronization; a separate voiceover is recommended.]

## Skill Version(s):

1.0.31 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
