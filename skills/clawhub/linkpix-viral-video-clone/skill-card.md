## Description:

This skill helps an agent analyze a short-video reference link, reverse-engineer the script and pacing, rewrite it for the user's product, and prepare a LinkPix video-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to turn a Douyin or TikTok-style reference video into a product-specific marketing video plan and LinkPix generation task. The workflow is useful when a user asks to make a similar, benchmark, or inspired version of a competitor or viral short video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys may be exposed if a user pastes a qhkit or LinkPix token into chat.

Mitigation: Have the user configure the token locally with qhkit or QHKIT_TOKEN, and advise revocation for any token already shared in a transcript.

Risk: The workflow uploads user media and reference material to the qhkit/LinkPix service for video generation.

Mitigation: Use the skill only when the user is comfortable sending those assets to the service, and avoid uploading sensitive media.

Risk: A generate action can consume credits and create a task that cannot be canceled.

Mitigation: Run estimates and present the key parameters for user confirmation before submitting any generation command.

Risk: Viral-video cloning can create intellectual-property or likeness concerns if it copies source material too closely.

Mitigation: Use the reference for structure, pacing, and creative direction while rewriting copy and replacing assets for the user's own product.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-viral-video-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include rewritten video scripts, qhkit command parameters, credit estimates, task IDs, status summaries, and generated video URLs.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
