## Description:

Helps TikTok Shop sellers and short-video commerce teams generate product hero images, carousel sets, detail images, campaign posters, and video cover images through Qinghu AI models via qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, creators, and cross-border commerce teams use this skill to create TikTok Shop-ready product images, carousel main-image sets, product detail images, and promotional campaign graphics. Agents use it to guide qhkit setup, choose the relevant image workflow, estimate generation cost, and submit image generation jobs after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may expose Qinghu API credentials if users paste keys directly into chat.

Mitigation: Configure credentials privately through a protected environment variable or local credential mechanism, and use limited, revocable keys with spending controls.

Risk: Product images are sent to Qinghu for image generation.

Mitigation: Use the skill only for images that are approved for third-party processing and avoid uploading confidential or restricted assets.

Risk: Installing or upgrading qhkit at runtime can change local command behavior.

Mitigation: Review package installation steps, prefer controlled environments, and verify qhkit configuration before submitting generation jobs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-tiktok-shop-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce or relay qhkit image-generation commands, configuration steps, cost estimates, and generated image URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
