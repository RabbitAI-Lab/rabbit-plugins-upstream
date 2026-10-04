## Description:

Guides agents in cloning a voice from a clean audio sample for use with ElevenLabs text-to-speech through dLazy's CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent through providing a voice sample and creating a custom voice for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded to dLazy-controlled services and may contain sensitive or unauthorized recordings.

Mitigation: Use only voice samples you are authorized to process and review dLazy's service terms before uploading.

Risk: The dLazy API key may be saved locally for reuse.

Mitigation: Protect the local key and rotate or revoke it if exposed or no longer needed.

Risk: Documentation examples and output format may not match the voice-cloning command.

Mitigation: Check the command's help and validate the returned result before relying on example fields.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions and shell commands; the CLI returns JSON with a result or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an audio sample and dLazy API key; generated results are hosted by dLazy.]

## Skill Version(s):

1.3.24 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
