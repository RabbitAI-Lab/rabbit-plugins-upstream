## Description:

This skill guides agents to use the qhkit/LinkPix CLI to replace e-commerce product models or faces in images and videos while preserving clothing, pose, composition, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to localize e-commerce model images or videos by replacing a model's appearance through LinkPix/qhkit. It is intended for authorized model or face replacement workflows, including country, skin-tone, and age localization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can replace the likeness of a real or recognizable person.

Mitigation: Confirm the user has rights to use the likeness before running model or face replacement, and refuse unauthorized requests.

Risk: The qhkit/LinkPix CLI may upload selected images or videos and use configured API credentials or credits.

Mitigation: Install and run the CLI only when third-party media processing is acceptable, protect configured tokens, and check credit estimates before generation.

Risk: Generated redraws may change product-critical details such as text, logos, or structure.

Mitigation: Review generated outputs before use and verify key product details before publishing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs are returned by the LinkPix/qhkit CLI; video jobs require status polling.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
