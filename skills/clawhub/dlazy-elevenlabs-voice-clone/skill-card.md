## Description:

Uploads a clean voice sample through the dLazy CLI to create an ElevenLabs instant voice clone for use with ElevenLabs TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to authenticate with dLazy, submit a voice sample, and request an ElevenLabs voice clone for downstream text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to upload sensitive voice samples.

Mitigation: Use only recordings that the user has rights to submit and for which the speaker has given explicit consent.

Risk: Uploaded audio and generated voice artifacts may leave the user's machine for dLazy or ElevenLabs processing.

Mitigation: Review the service terms and avoid submitting confidential or regulated audio unless that processing is approved.

Risk: The documentation is inconsistent about required flags, command examples, and returned output.

Mitigation: Run help or dry-run commands before production use and verify the actual command, required inputs, and response shape.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; may return hosted output URLs or asynchronous task IDs.]

## Skill Version(s):

1.3.11 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
