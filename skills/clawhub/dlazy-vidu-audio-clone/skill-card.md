## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to clone an owned or permitted reference voice and generate new speech from supplied text through the dLazy Vidu Audio Clone CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning may enable unauthorized impersonation or use of third-party audio.

Mitigation: Use only voices and recordings you own or have explicit permission to clone, and review outputs for impersonation or consent issues before sharing.

Risk: Prompts, parameters, and referenced audio files may be sent to dLazy-hosted endpoints.

Mitigation: Avoid sensitive or private audio and text, and review dLazy service terms and privacy expectations before use.

Risk: The skill relies on an external npm CLI package and offers a global install path.

Mitigation: Prefer the pinned npx invocation when possible, and review the @dlazy/cli package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs or async task status, plus Markdown guidance for authentication and errors]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may upload referenced audio files and prompts to dLazy-hosted endpoints.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
