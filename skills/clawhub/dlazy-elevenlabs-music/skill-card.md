## Description:

ElevenLabs music_v1 model — generates 10–300s original music from a natural-language prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can request original music for background tracks, advertisements, and short-form videos by providing a natural-language prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and reports that the documented music-generation behavior was not corroborated by the commands it analyzed.

Mitigation: Review the pinned CLI package and its credential setup before use, and confirm that the installed command performs the expected generation task.

Risk: Use requires a dLazy API key, which the CLI can store in the user's local configuration; prompts are sent to the hosted dLazy API.

Mitigation: Review the credential and service details before sending prompts, protect the key, and rotate or revoke it if exposed.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio files (documented output), JSON result metadata]

**Output Format:** [Generated media asset URL with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documented music duration is 10–300 seconds (30 seconds by default); asynchronous runs may return a task identifier. The supplied example labels its media output as an image, and the security review flags that generation behavior was not corroborated.]

## Skill Version(s):

1.3.41 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
