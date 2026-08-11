## Description:

Converts images into PPT files asynchronously through the Scnet OCR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and workflow agents use this skill to submit a local image to Scnet, poll for conversion completion, and receive a temporary download link for the generated PPTX file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected image or document content is uploaded to Scnet for processing.

Mitigation: Use the skill only for files appropriate for third-party processing, and check Scnet data-handling terms before using sensitive content.

Risk: Successful conversions return temporary external download links.

Mitigation: Download results promptly and avoid sharing generated links beyond the intended recipients.

Risk: The skill requires a Scnet API key.

Mitigation: Store the key in an environment variable or local config file and do not paste secrets into chat.

## Reference(s):

- [Scnet Document Conversion API Docs](references/api-docs.md)
- [Server-resolved GitHub Source](https://github.com/SCNet-sugon/image_to_ppt)
- [Scnet Website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON containing task metadata and temporary PPTX download links, with user-facing error text on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Scnet API key and uploads the selected local image to a third-party conversion service.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
