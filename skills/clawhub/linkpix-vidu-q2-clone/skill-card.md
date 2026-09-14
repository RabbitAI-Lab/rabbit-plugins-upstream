## Description:

Vidu Q2 爆款视频复刻 | LinkPix helps sellers analyze a viral video link, rewrite its structure for their own product, and generate a Vidu Q2-style short commerce video through qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and content operators use this skill to turn a short-video reference link into a script comparison, product-specific rewrite, and qhkit video generation workflow for Vidu Q2-style ecommerce content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may expose qhkit API credentials if users paste keys directly into chat.

Mitigation: Use a protected local secret mechanism such as QHKIT_TOKEN and avoid sharing raw API keys in conversation.

Risk: Mutable install commands such as package installs without version pins can change behavior over time.

Mitigation: Pin and locally review qhkit versions before installation or upgrade.

Risk: Uploaded media filenames or metadata may contain sensitive or unsafe content.

Mitigation: Sanitize or rename uploaded media files before running compression or generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys page](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline qhkit command examples and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce script rewrites, task status guidance, and video result links after qhkit execution.]

## Skill Version(s):

0.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
