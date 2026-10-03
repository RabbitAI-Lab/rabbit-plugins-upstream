## Description:

Guides an agent in cloning an authorized voice sample for use with ElevenLabs text-to-speech through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create a custom voice from an authorized recording for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning without the speaker's authorization could enable impersonation.

Mitigation: Use only recordings you own or have explicit permission to clone.

Risk: Voice recordings are uploaded to dLazy services and may be subject to provider retention practices.

Mitigation: Review dLazy and ElevenLabs privacy and retention terms before uploading sensitive audio.

Risk: Installing the CLI and supplying a dLazy API key exposes local credentials to the chosen tool.

Mitigation: Review the pinned CLI before installation and protect or rotate the API key as needed.

Risk: The documented image output and --prompt examples conflict with voice-cloning usage.

Mitigation: Check the command help and actual response before relying on those examples.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return a result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.23 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
