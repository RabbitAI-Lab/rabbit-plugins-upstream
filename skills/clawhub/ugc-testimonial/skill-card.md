## Description:

UGC 口播种草视频。商品 + 人设 → 口播脚本与成片，达人自拍质感。当用户说「口播视频」「种草视频」「达人风格」「UGC」「真人推荐」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Commerce and creative teams use this skill to draft short UGC-style product scripts and storyboards, then generate testimonial-style product videos for review and campaign testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generation may send prompts and reference images to the selected external provider; the security review reports an external-data disclosure concern and incomplete inspection.

Mitigation: Before running generation, confirm which provider is configured and what information it receives. Avoid sending sensitive images or personal information unless that transfer is authorized.

Risk: UGC-style generated scripts or videos could be mistaken for genuine customer testimonials.

Mitigation: Present generated scenes as demonstrations, do not attribute them to real buyers, and follow the target platform's AI-content labeling rules.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [Video backend configuration](references/video-backends.md)
- [Brand kit model reference guidance](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Storyboard JSON, Shell commands, Configuration, Video files]

**Output Format:** [Scripts and storyboards in Markdown or JSON, commands and configuration in shell or YAML, and generated video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include subtitles; generated footage does not provide reliable lip synchronization, so narration may need to be added during editing.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
