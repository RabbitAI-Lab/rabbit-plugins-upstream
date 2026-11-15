## Description:

Image Upscaler is an AI-powered image enhancement skill for sharpening blurry images, clarifying thumbnails, and performing 2x/4x lossless upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[steinvenic](https://clawhub.ai/user/steinvenic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit an image to a hosted enhancement API, poll for task status, and retrieve the processed image URL when upscaling or deblurring completes.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Image files and API keys are sent to the provider's external server.

Mitigation: Use the skill only with a trusted provider account, avoid submitting private or regulated images unless provider privacy and retention terms are acceptable, and handle the API key as a sensitive credential.

Risk: Service availability is limited to mainland China.

Mitigation: Confirm the user and runtime can access the hosted endpoint before relying on the skill in a workflow.

## Reference(s):

- [OpenAPI specification](artifact/openapi.yaml)
- [ClawHub skill page](https://clawhub.ai/steinvenic/skills/image-upscaler)

## Skill Output:

**Output Type(s):** [text, shell commands, API calls, guidance]

**Output Format:** [Markdown guidance with JSON API responses and image result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an API key and sends image files to the provider's hosted service.]

## Skill Version(s):

1.0.0 (source: release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
