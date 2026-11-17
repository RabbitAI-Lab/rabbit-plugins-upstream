## Description:

Generate realistic digital human broadcast videos from portrait images and audio/text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate digital human broadcast videos from a portrait image and audio or a text prompt through dLazy's Jimeng OmniHuman 1.5 service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a partial scan and a purpose mismatch between the expected video generation task and behavior described in the supplied material.

Mitigation: Review the CLI help and unresolved referenced material before installing or relying on the skill.

Risk: Local image and audio inputs are uploaded to dLazy-hosted media storage for processing.

Mitigation: Use media you are authorized to share with the service, and avoid uploading sensitive material unless the service's handling terms are acceptable.

## Reference(s):

- [dLazy service homepage](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video assets, JSON, Files]

**Output Format:** [JSON response containing generated media URLs, optionally with a saved local media file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to one portrait image and one audio input; supports 720p or 1080p output. Audio duration limits are 60 seconds at 720p and 30 seconds at 1080p.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
