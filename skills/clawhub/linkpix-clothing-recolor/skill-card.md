## Description:

This skill guides an agent through using LinkPix qhkit image generation to create recolored clothing product images for SKU variants while preserving garment shape, material texture, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to create recolored clothing SKU images from a source garment photo without reshooting. It is suited to product listing color variants where users need LinkPix/qhkit guidance and shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may add or upgrade a global qhkit CLI, which can change the execution environment.

Mitigation: Use a pinned, reviewed qhkit version in an isolated environment and review install or upgrade commands before execution.

Risk: The workflow stores or uses a LinkPix token.

Mitigation: Use environment-based secret handling where possible, keep tokens out of logs and prompts, and rotate or revoke tokens if exposed.

Risk: Selected garment images are uploaded to the LinkPix service for processing.

Mitigation: Confirm the images are appropriate to upload and avoid sending confidential, private, or unlicensed assets.

Risk: Generated recoloring is not pixel-level editing and may alter product details such as text, logos, or garment structure.

Mitigation: Review generated images against the source product before publication, especially brand marks, printed text, and structural details.

Risk: Tool output may include shell commands that should not be executed blindly.

Mitigation: Have a human review shell commands copied from tool output before running them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent to return generated image URLs and qhkit credit usage after command execution.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
