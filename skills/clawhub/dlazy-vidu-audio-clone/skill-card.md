## Description:

Clone a voice from reference audio and generate spoken audio from new text with Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can provide reference audio and text to generate speech in a cloned voice. The skill sends prompts and audio inputs to dLazy-hosted services for processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio and prompts are sent to dLazy-hosted services, and local audio paths are uploaded to dLazy media storage.

Mitigation: Only submit recordings you have permission to share and that are appropriate for cloud processing.

Risk: The skill relies on the dLazy CLI and an API key stored in the user's configuration or supplied through an environment variable.

Mitigation: Review the CLI source and pinned package version before installation, protect the API key, and rotate or revoke it if needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated audio hosted at a URL, with a JSON result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task ID and status before audio is ready.]

## Skill Version(s):

1.3.39 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
