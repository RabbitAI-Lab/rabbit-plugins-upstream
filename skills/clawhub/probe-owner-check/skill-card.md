## Description:

Creates and edits images with AdsTurbo, including text-to-image, image editing, background removal, product images, campaign posters, watermark or object removal, and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and commerce operators use this skill to generate or edit AdsTurbo-hosted image assets for product listings, campaign posters, background removal, object removal, and upscaling. It is intended for workflows where the user can provide an AdsTurbo API key and public media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image, audio, video, or other files can be uploaded to AdsTurbo and returned as public URLs.

Mitigation: Use only assets the user is authorized to send to AdsTurbo, avoid private or regulated data, and prefer existing public URLs when appropriate.

Risk: The generic file and audio upload commands can send non-image files beyond the main image-generation use case.

Mitigation: Use the generic upload paths only when the downstream task explicitly requires them and the user understands what file is being uploaded.

Risk: Watermark or object removal can be misused on media the user is not authorized to alter.

Mitigation: Confirm the user has rights to edit the media and decline requests that appear to remove ownership, attribution, or access-control markings without authorization.

## Reference(s):

- [Image generation and editing reference](references/image.md)
- [Media upload reference](references/upload.md)
- [Async work status reference](references/work.md)
- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/probe-owner-check)
- [AdsTurbo website](https://www.adsturbo.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with image links and inline shell commands; supporting scripts emit JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADSTURBO_API_KEY and publicly accessible media URLs; asynchronous tasks may return workspace IDs for polling.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
