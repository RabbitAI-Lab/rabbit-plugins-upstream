## Description:

AI 自动优化商品主图的构图、光影、质感及细节，提升商品吸引力与点击率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and agents use this skill to improve product main images with LinkPix/qhkit by preserving the product subject while enhancing composition, lighting, texture, detail, and click-through appeal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade the qhkit npm CLI and supporting Node tooling.

Mitigation: Require explicit user approval before package installation or upgrade, and prefer an isolated environment.

Risk: Using qhkit can upload local product images to the LinkPix service.

Mitigation: Confirm the user intends to use LinkPix/qhkit for the selected images before running generation commands.

Risk: API-token setup is required for service access.

Mitigation: Avoid pasting long-lived secrets into chat or shell history; prefer environment-based token handling where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit commands that upload local product images and return generated image URLs with credit usage.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
