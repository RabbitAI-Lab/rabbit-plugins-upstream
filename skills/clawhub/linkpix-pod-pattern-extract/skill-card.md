## Description:

Extracts print patterns from product or apparel images into high-resolution, tiled bitmap design assets for POD customization and clothing design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative operators use this skill to turn visible apparel or product prints into reusable POD pattern assets through the LinkPix/qhkit image workflow. It is intended for pattern extraction, materialization, and follow-on design review, with users expected to check generated details for fidelity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update local Node-based tooling before running the image workflow.

Mitigation: Review the qhkit package installation step and install only in environments where adding local command-line tools is acceptable.

Risk: Selected images are sent to the qhkit/LinkPix service for processing.

Mitigation: Use only images that are appropriate to upload to the service and avoid submitting confidential or unlicensed content.

Risk: API keys may be requested for service configuration.

Mitigation: Use a scoped, revocable token where possible, avoid sharing long-lived credentials in chat, and rotate the token after use.

Risk: Generated pattern extraction may differ from the source print or reproduce protected brand/IP elements.

Mitigation: Review the generated asset for fidelity and rights concerns before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix/Qinghu workspace](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit shell commands and generated image URLs from the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local image inputs or image URLs, qhkit installation, and a configured Qinghu/LinkPix API token.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
