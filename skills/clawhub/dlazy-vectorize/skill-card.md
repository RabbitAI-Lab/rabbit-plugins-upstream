## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns the URL, suitable for lossless scaling and vectorization of logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and external users use this skill to convert PNG/JPG assets such as logos, icons, and flat illustrations into scalable SVG outputs through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image files passed to the skill may be uploaded to dLazy's hosted service for processing.

Mitigation: Only process images approved for dLazy cloud handling and avoid sending sensitive assets unless the service terms meet the user's requirements.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY or npx for less persistent setup, and rotate or revoke keys from dLazy when needed.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Review sharing and retention expectations for hosted output URLs, or save approved results locally with --save.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [JSON CLI response with hosted result URL; optional local file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may return an asynchronous task id when --no-wait is used.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
