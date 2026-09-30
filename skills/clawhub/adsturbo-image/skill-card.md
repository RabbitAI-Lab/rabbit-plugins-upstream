## Description:

Creates and edits images for e-commerce and marketing, including product images, posters, background removal, object removal, and upscaling through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to generate or edit campaign and product images, remove backgrounds or objects, and upscale images using an AdsTurbo API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading local images, audio, or other files makes them available at public URLs and sends them to a third party.

Mitigation: Upload only media you own or may use, and avoid confidential files or personal voice samples unless public exposure and third-party processing are acceptable.

Risk: Watermark removal can violate ownership or usage rights.

Mitigation: Remove watermarks only when authorized by the rights holder.

Risk: An exposed API key could enable unauthorized use of the AdsTurbo account.

Mitigation: Keep the AdsTurbo API key in the environment and do not include it in replies or shared files.

Risk: The skill depends on the Python requests package for network access.

Mitigation: Consider pinning and auditing the dependency before deployment.

## Reference(s):

- [AdsTurbo Image Creation on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-image)
- [Image commands and model capabilities](references/image.md)
- [Media upload guidance](references/upload.md)
- [Asynchronous work status](references/work.md)
- [AdsTurbo API key setup](https://adsturbo.ai/iris/api)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with generated image links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image operations return hosted image URLs; asynchronous jobs may require status polling.]

## Skill Version(s):

1.2.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
