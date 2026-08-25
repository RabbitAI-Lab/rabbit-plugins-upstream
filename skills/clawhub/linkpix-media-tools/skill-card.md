## Description:

LinkPix Media Tools helps agents route video watermark removal, subtitle removal, super-resolution, image editing, compression, and watermarking requests through the qhkit command-line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to prepare ecommerce and social media assets by selecting the right LinkPix/qhkit workflow for video cleanup, video enhancement, product image editing, compression, or watermarking. The skill also guides setup, cost confirmation, task polling, and delivery of generated media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the qhkit command-line package.

Mitigation: Review the package source and requested install path before deployment, and prefer a managed environment with pinned package versions.

Risk: The workflow can configure and use a Qinghu API key on the local machine.

Mitigation: Use a limited API key, avoid sharing secrets in chat history, and rotate or revoke the key when access is no longer needed.

Risk: Local images or videos may be uploaded to the LinkPix/Qinghu service for processing.

Mitigation: Do not submit sensitive media or third-party-owned assets unless the user confirms they have rights and approval to process them.

Risk: Generate actions may consume paid credits and cannot be canceled after submission.

Mitigation: Run estimates when available and obtain explicit user confirmation of key parameters and expected charges before submitting generation tasks.

Risk: Watermark removal or subtitle removal can create copyright or licensing concerns.

Mitigation: Ask the user to confirm appropriate rights before assisting with removal workflows, especially for commercial use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-media-tools)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status summaries, generated media URLs, and credit usage when processing tasks complete.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
