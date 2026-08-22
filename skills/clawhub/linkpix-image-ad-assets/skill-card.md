## Description:

自动生成适用于电商推广及广告投放的图文营销素材：广告图片、促销图，以及从视频反推的图文种草内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill to generate e-commerce ad images, promotional graphics, and text-and-image product seeding content from product inputs or short-form videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the host-level qhkit package.

Mitigation: Review installation behavior before use and prefer scoped or explicit installation paths when host-level package changes are not acceptable.

Risk: The skill can reuse an existing OpenClaw Qinghu token and submit credit-consuming generation jobs.

Mitigation: Confirm the account, token, uploaded files, generation parameters, and estimated credits before any generate action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with generated asset links, text content, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image URLs and generated marketing copy; generation commands can consume qhkit credits after user confirmation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
