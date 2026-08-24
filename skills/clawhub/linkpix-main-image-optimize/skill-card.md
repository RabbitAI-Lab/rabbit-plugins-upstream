## Description:

AI 自动优化商品主图的构图、光影、质感及细节，提升商品吸引力与点击率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce teams and agents use this skill to decide when to improve a product main image and to guide qhkit/LinkPix image generation for higher-quality product visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for an API key in chat.

Mitigation: Prefer setting QHKIT_TOKEN or configuring qhkit directly in a local terminal, and do not paste API keys into chat.

Risk: The skill can use an existing local qhkit/LinkPix token and submit image-generation jobs that consume credits.

Mitigation: Review token use, image uploads, and credit estimates before approving generation.

Risk: Generated product images may alter visible product details.

Mitigation: Check text, logos, product structure, and other critical details before using generated images commercially.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline bash commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide image upload, credit estimation, user confirmation, generation, and delivery of image URLs.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
