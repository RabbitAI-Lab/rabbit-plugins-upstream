## Description:

根据商品卖点自动生成带货文案与视频脚本，支持口播、种草、测评、剧情等风格；也能从对标爆款视频反推脚本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce operators use this skill to generate product sales scripts, spoken promotional copy, seeding copy, review scripts, story-driven video scripts, and scripts reverse-engineered from comparable popular videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle a LinkPix API key and the security evidence notes that the key can be requested in chat and stored locally.

Mitigation: Use a platform secret store or environment variable such as QHKIT_TOKEN, avoid pasting secrets into chat, and review local qhkit configuration before sharing logs or workspaces.

Risk: The skill can submit credit-consuming LinkPix storyboard or video-inspiration tasks.

Mitigation: Confirm product images, selling points, source video links, language, and other task parameters with the user before every submission.

Risk: The skill may install Node/qhkit tooling or download Node binaries when local dependencies are missing.

Mitigation: Review install commands before execution, prefer trusted package sources, verify downloaded checksums where provided, and use least-privilege installation paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-sales-script)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and complete generated script text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a LinkPix API key, and user confirmation before credit-consuming script generation submissions.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
