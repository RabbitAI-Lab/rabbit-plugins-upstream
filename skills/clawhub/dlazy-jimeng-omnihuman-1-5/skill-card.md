## Description:

Generates realistic digital presenter videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to create presenter-style videos from a portrait image and audio or text. It sends the generation request to dLazy's hosted service and returns the resulting media asset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and portrait or audio media are sent to dLazy's hosted API and media storage for generation.

Mitigation: Avoid submitting sensitive or non-consensual media, and review dLazy's service terms and privacy practices before use.

Risk: The security scan was partial and could not resolve several references, including the CLI package.

Mitigation: Review the published CLI package and its source before installing it if you need to assess that dependency.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Files, API Calls]

**Output Format:** [Generated video asset URL or locally saved video file, with JSON status and result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one portrait image and audio or text prompt; supports 720p and 1080p output.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
