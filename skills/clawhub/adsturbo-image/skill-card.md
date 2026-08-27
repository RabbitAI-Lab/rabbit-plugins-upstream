## Description:

Text-to-image generation and image editing, plus a full e-commerce toolkit: background removal, product/scene/detail shots, campaign posters, watermark removal, and upscaling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, edit, retouch, upload, and track image assets for AdsTurbo e-commerce and marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Watermark or object removal can be misused on media the user does not own or have permission to edit.

Mitigation: Use removal features only for owned or authorized content, and confirm the user's rights before processing third-party media.

Risk: Local media uploads are sent to AdsTurbo and returned as public URLs.

Mitigation: Do not upload sensitive local files unless the user accepts third-party processing and public URL exposure; use already-public URLs when possible.

Risk: The skill depends on an unpinned requests version range.

Mitigation: Pin requests to a reviewed safe version in managed deployments.

Risk: Model-specific capability, ratio, and resolution mismatches can cause rejected image requests.

Mitigation: Check the model capability table before choosing text-to-image, editing, ratio, or resolution parameters.

## Reference(s):

- [AI Image Creation / Image](artifact/references/image.md)
- [Upload](artifact/references/upload.md)
- [Work Status](artifact/references/work.md)
- [AdsTurbo API Key Signup](https://adsturbo.ai?channel=clawhub)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-image)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands; scripts emit JSON responses, image URLs, public upload URLs, or workspace IDs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async operations poll for completion by default; media inputs must be public URLs or uploaded first.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
