## Description:

为电商推广和广告投放生成广告图片、促销图，并可将带货视频转换为图文种草内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, content operators, and agent users use this skill to produce image ads, promotional visuals, and social commerce text assets from product images or source videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the skill may add a persistent qhkit CLI to the user's environment.

Mitigation: Install qhkit only when this service dependency is acceptable, and use user-scoped installation or npx when global installation is not appropriate.

Risk: The workflow may request a LinkPix/qinghu API key and upload local media files to the service.

Mitigation: Use a dedicated token, avoid sensitive media, and proceed only when the service credential and upload flow is acceptable.

Risk: Generation actions can spend account credits.

Mitigation: Run estimates when supported, report expected credits, and require explicit user confirmation before submitting paid generation tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API Keys Console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with qhkit shell commands, JSON parameters, image URLs, and generated marketing copy.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require qhkit installation, a LinkPix/qinghu API key, local media upload, credit estimation, and user confirmation before paid generation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
