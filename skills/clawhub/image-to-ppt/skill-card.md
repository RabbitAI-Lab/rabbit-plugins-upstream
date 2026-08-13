## Description:

Converts image files into PPTX presentations asynchronously using the Scnet OCR conversion service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to submit local image files for cloud conversion into editable PowerPoint files and retrieve the resulting temporary download link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to Scnet for cloud conversion, which can expose confidential, regulated, or private content to an external service.

Mitigation: Use the skill only for images approved for that data flow, and avoid confidential or regulated files unless the organization has approved Scnet processing.

Risk: The configurable SCNET_API_BASE controls the conversion endpoint and could route files or credentials to an untrusted service if changed.

Mitigation: Keep SCNET_API_BASE pointed at a trusted Scnet endpoint and review configuration before execution.

Risk: SCNET_API_KEY is required for operation and may be exposed if pasted into chat or stored with overly broad file permissions.

Mitigation: Provide the key through environment variables or a protected local config file and do not paste credentials into agent conversations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/image-to-ppt)
- [Source repository](https://github.com/SCNet-sugon/image_to_ppt)
- [Scnet website](https://www.scnet.cn)
- [Scnet API documentation](references/api-docs.md)
- [Response fields summary](assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [JSON result with task metadata and temporary PPTX download URLs, plus human-readable error text on failure.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads selected image files to Scnet for cloud conversion.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
