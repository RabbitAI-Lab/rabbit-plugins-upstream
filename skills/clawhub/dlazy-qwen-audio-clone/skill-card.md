## Description:

Clones a custom voice from a clean sample for subsequent Alibaba Bailian Qwen3-TTS calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators can submit a clean voice sample to create a custom voice for later text-to-speech calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the advertised voice-cloning purpose and observed CLI login behavior, with partial analysis and unresolved references.

Mitigation: Review the resolved CLI command and package before installing or providing credentials, and confirm the workflow matches the intended task.

Risk: The documented workflow sends prompts to a hosted service and uploads local audio samples for processing.

Mitigation: Confirm you have permission to share the voice sample and prompts with the hosted service before submitting them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [CLI project homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Media URLs]

**Output Format:** [JSON response with generation status and output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs may return a task ID for status polling.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
