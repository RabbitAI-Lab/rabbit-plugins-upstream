## Description:

青虎AI 图片高清写实去 AI 感：极速出图，增强画面细节、去除 AI 生成图片的油腻失真感、提升画面统一度并减少图像偏移，快速得到写实高清图像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to enhance one local or hosted image at a time by reducing visible AI-generated artifacts, improving realistic detail, and returning generated image options for user selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a mutable global npm CLI that handles local images and service credentials.

Mitigation: Install only after reviewing and trusting @iqinghu/qhkit and the Qinghu service; prefer a pinned reviewed package version over automatic @latest upgrades or npx fallback.

Risk: The workflow submits user images and an API token to an external service that may bill for generation.

Mitigation: Use only authorized images, protect the API token, run estimate with the same parameters before generation, and confirm the estimated credit cost with the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-deai-hd)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and image result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return multiple generated image URLs; agents should present all returned options and report actual consumed credits when generation succeeds.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
