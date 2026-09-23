## Description:

Alibaba Bailian qwen3-tts text-to-speech lets agents choose curated system voices, including dialects, or design a custom voice from a natural-language description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate speech from text through dLazy's hosted Qwen TTS wrapper, selecting system voices or describing a custom voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and generation parameters are sent to dLazy's hosted API.

Mitigation: Review user content before sending it to the service and avoid submitting sensitive text unless the deployment has approved dLazy for that data.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The artifact's documented output example appears to describe image/png output even though this is a text-to-speech skill.

Mitigation: Treat the output schema example as documentation that needs confirmation and verify returned MIME types and saved files during integration testing.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-tts)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with generated asset URLs, optional downloaded files, and brief command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and network access to api.dlazy.com and files.dlazy.com; supports async task IDs via --no-wait.]

## Skill Version(s):

1.3.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
