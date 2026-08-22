## Description:

Nano Banana 2 图片编辑 helps agents edit existing images with Nano Banana 2 through AI Hive, covering cleanup, object replacement, color changes, composition revisions, localized people or product edits, and channel-specific variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and commerce teams use this skill to prepare image-edit prompts, submit source images to AI Hive, and review generated edits for cleanup, replacement, recoloring, layout adaptation, and batch variants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected source images and prompts are sent to AI Hive for processing.

Mitigation: Use explicit image paths and avoid submitting sensitive or non-image files unless sharing them with AI Hive is acceptable.

Risk: An AI Hive API key may be stored locally for repeated use.

Mitigation: Review the local configuration before sharing the machine and prefer environment variables or key rotation when operational policy requires it.

Risk: Image edits may introduce unintended visual changes to people, products, text, logos, or composition.

Mitigation: Compare each output with the source image and verify requested and unrequested changes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-image-edit)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompt text, one or more image paths, optional batch size, routing mode, model parameters, and output directory; generated images are downloaded unless no-download is selected.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
