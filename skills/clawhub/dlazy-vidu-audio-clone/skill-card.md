## Description:

Uses a reference voice sample to generate spoken audio for new text through Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use the skill to generate new spoken audio from text using a reference voice sample and dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning a voice without the speaker's rights or consent can enable impersonation.

Mitigation: Confirm rights or consent for each voice sample before generating audio.

Risk: Voice samples and prompts supplied to the hosted service are uploaded to dLazy endpoints.

Mitigation: Use the service only when uploading those materials is acceptable.

Risk: Logging in can store an API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per run if persistent local key storage is unsuitable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [JSON result with generated audio links or asynchronous task status; command guidance in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and a voice sample; asynchronous jobs may need status polling.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
