## Description:

Generates multiple POD print design variations from one reference pattern by varying colors, styles, and element combinations with LinkPix/qhkit image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, POD sellers, and agent operators use this skill to turn a single print into a family of related design options for SKU expansion, colorway exploration, and theme-specific variations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install qhkit or related tooling in the agent environment.

Mitigation: Install only in environments where agent-managed npm tooling is acceptable, and review installation commands before running them.

Risk: Referenced design images may be uploaded to the LinkPix/qhkit service.

Mitigation: Use images that are approved for upload to third-party services and avoid sensitive or unlicensed assets.

Risk: Generation requests can consume LinkPix/qhkit credits.

Mitigation: Review the model, image count, size, referenced inputs, and estimate before approving any generation request.

Risk: Generated pattern variations may alter important details from the source print.

Mitigation: Inspect generated outputs for key elements, style consistency, and production suitability before publishing or selling them.

Risk: The workflow may require storing or using a qhkit API token.

Mitigation: Provide tokens only through approved secret-handling paths and rotate or revoke them if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-variations)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qhkit API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit commands that upload referenced design images and can consume LinkPix/qhkit credits after user approval.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
