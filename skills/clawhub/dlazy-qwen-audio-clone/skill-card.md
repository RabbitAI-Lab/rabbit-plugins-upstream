## Description:

This skill uses Alibaba Bailian qwen3-tts to clone a custom voice from a clean audio sample for later text-to-speech use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to create a reusable custom voice from a clean audio sample for later text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to dLazy for processing.

Mitigation: Confirm you have permission to use the sample and review the service's retention terms before uploading it.

Risk: Requests consume account credits.

Mitigation: Use the documented dry-run option to preview the estimated cost before making a request.

Risk: The CLI can save an API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication if you prefer not to store the key in the CLI configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Configuration instructions]

**Output Format:** [JSON response with the voice-cloning result or an asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a reusable hosted voice profile from a supplied audio sample.]

## Skill Version(s):

1.3.35 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
