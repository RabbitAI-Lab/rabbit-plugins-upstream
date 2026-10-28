## Description:

Generate realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to generate digital-human broadcast videos from a portrait image and audio or text with Jimeng OmniHuman 1.5.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portrait images, audio, and prompts are sent to dLazy cloud services for generation.

Mitigation: Submit only media and prompts you are authorized to share with the service.

Risk: Login stores an API key in the local dLazy CLI configuration.

Mitigation: Protect the local configuration, use an organization-scoped key, and rotate or revoke it if exposed.

Risk: Video generation consumes account credits.

Mitigation: Use --dry-run to preview the request and estimated cost before generation.

Risk: Installing the CLI adds a third-party package to the environment.

Mitigation: Review the pinned @dlazy/cli version before installing.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Hosted video asset URLs in a JSON API response, with an optional saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation is asynchronous; audio input supports up to 30 seconds at 1080p or 60 seconds at 720p.]

## Skill Version(s):

1.3.34 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
