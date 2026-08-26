## Description:

AdsTurbo AI Image Creation helps agents generate, edit, retouch, and upscale images, including e-commerce product sets and marketing posters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and edit commercial image assets with AdsTurbo, including product images, campaign posters, cutouts, object or watermark removal, and upscaling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports watermark or object removal, which can be misused on third-party images.

Mitigation: Confirm that the user owns the image or has permission before removing watermarks, attribution, or protected content.

Risk: The security review marked the release suspicious because the artifact normalizes watermark removal without ownership or permission checks.

Mitigation: Review use cases before installation when users may process third-party images, and apply explicit policy checks around removal requests.

Risk: The artifact depends on the requests package without a pinned version.

Mitigation: Pin or constrain dependency versions before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/adsturbo-image)
- [AdsTurbo website](https://www.adsturbo.ai)
- [AI Image Creation reference](references/image.md)
- [Upload reference](references/upload.md)
- [Work Status reference](references/work.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and generated image links or task status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include AdsTurbo image URLs, workspace IDs for asynchronous jobs, and concise retry guidance for parameter mismatches.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
