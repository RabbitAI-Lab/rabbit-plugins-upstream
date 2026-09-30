## Description:

帮助代理使用 qhkit 生成电商商品主图、场景图、详情页、促销海报、广告图片和广告视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and operators use this skill to plan and generate bundled product-promotion assets such as main images, detail pages, campaign posters, ad images, and short ad videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prompt an agent to install or update qhkit, install Node, change PATH, or edit shell profile configuration.

Mitigation: Require explicit user confirmation before npm installs, npx runs, PATH changes, shell-profile edits, or tool upgrades.

Risk: The skill uses an external Qinghu service and may upload local product media for generation.

Mitigation: Confirm with the user before uploading files or URLs, and avoid submitting confidential or unapproved product media.

Risk: The skill requires qhkit credential configuration and may initiate paid image or video generation.

Mitigation: Confirm before token configuration and before any paid generation; report the estimated credits and balance status before submitting jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-marketing-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit credit estimates, task status, generated image URLs, generated video URLs, and failure messages returned by the CLI.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
