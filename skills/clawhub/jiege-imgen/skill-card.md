## Description:

使用兼容 OpenAI Images API 的网关生成、编辑和落地项目图片素材；用户要求生图、画图、改图、修图、换风格、扩图、去背景、抠图，或需要 Logo、应用图标、Banner、封面、插图、背景图、空状态图、宣传图和产品视觉素材时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tans](https://clawhub.ai/user/tans)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or edit project image assets through an OpenAI Images API-compatible gateway, save PNG files into project asset paths, and connect generated assets to the project when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an API key to a default or user-configured image gateway.

Mitigation: Use only a trusted endpoint, override the base URL when appropriate, and prefer a dedicated, revocable API key.

Risk: The skill can write generated files into the project workspace.

Mitigation: Confirm the requested output path before execution and review any project asset references added after generation.

Risk: An optional auth file can provide credentials to the image service.

Mitigation: Pass an auth file only when it contains credentials intended for this image service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tans/skills/jiege-imgen)
- [Default compatible image gateway](https://token.minapp.xin/v1)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Configuration, Guidance]

**Output Format:** [PNG image files with Markdown or JSON status output and optional project code or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes PNG files to explicit project paths, may update asset references, and reports the resolved output path plus the Images API route used.]

## Skill Version(s):

0.1.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
