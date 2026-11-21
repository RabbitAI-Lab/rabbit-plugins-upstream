## Description:

Clone a voice from reference audio and generate spoken audio for new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to make spoken audio in a cloned voice from reference audio and new text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied partial scan noted a mismatch between the voice-cloning description and a reported login-only command, as well as hidden whitespace; its benign verdict is not a guarantee of safety.

Mitigation: Review the padded section of the Chinese guide and verify the CLI behavior and unavailable referenced paths before installation, as advised by the security assessment.

Risk: Reference audio and prompts are sent to dLazy's hosted service, and local audio paths are uploaded for processing.

Mitigation: Only submit audio and text you are authorized to share with the service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Shell commands]

**Output Format:** [Generated audio with a JSON response containing output links or an asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; audio and prompts are sent to the hosted service. Asynchronous runs may return a task ID before audio is ready.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
