## Description:

Converts image files into editable Word documents using Scnet OCR through an asynchronous API workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to submit local image files to Scnet, poll for OCR conversion completion, and return a temporary link to the generated editable Word document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are sent to Scnet for remote processing.

Mitigation: Use the skill only for documents approved for third-party processing and avoid sensitive images unless authorized.

Risk: The skill returns temporary remote download URLs for generated Word files.

Mitigation: Treat returned URLs as private secrets and download or dispose of them according to the user's data handling policy.

Risk: The Scnet API key is required for operation.

Mitigation: Store SCNET_API_KEY in an environment variable or a chmod-600 .env file and never paste credentials into chat.

## Reference(s):

- [Scnet Image to Word API Documentation](references/api-docs.md)
- [Source Repository](https://github.com/SCNet-sugon/image_to_word)
- [ClawHub Skill Page](https://clawhub.ai/scnet-sugon/skills/image-to-word)
- [Scnet Website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, files]

**Output Format:** [JSON containing task metadata and temporary .docx download links, with human-readable error messages on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY, uploads selected images to Scnet for processing, polls asynchronously, and returns temporary private download URLs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
