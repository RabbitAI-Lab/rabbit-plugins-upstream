## Description:

快速生成双11、黑五、圣诞节等营销活动海报与折扣营销图，适用于新品发布、促销活动及品牌宣传。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to generate LinkPix/qhkit promotional posters, discount marketing images, seasonal campaign graphics, and product launch visuals from text prompts and optional product images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can expose a LinkPix/qhkit API key if users paste secrets into chat.

Mitigation: Use a secure secret-entry mechanism or environment variable such as QHKIT_TOKEN, and rotate any token that was shared in chat.

Risk: The skill installs and runs local command-line tooling before generating images.

Mitigation: Review installation commands and install only the expected @iqinghu/qhkit package from a trusted registry.

Risk: Referenced product images are uploaded to the external LinkPix/qhkit service.

Mitigation: Confirm the user has rights to upload the images and avoid sending sensitive or confidential assets.

Risk: Image generation consumes account credits after task submission.

Mitigation: Run an estimate when available and obtain explicit user approval before running a generate command.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit image generation commands and returns generated image URLs after the external service completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
