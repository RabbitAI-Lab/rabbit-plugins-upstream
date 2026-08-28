## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's hosted Vidu Audio Clone service through the dLazy CLI, providing a text prompt and optional reference audio to generate cloned-voice speech. It is suited to authorized voice-cloning workflows where generated audio URLs or asynchronous task IDs are acceptable outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local audio files passed to the skill are uploaded to dLazy's hosted service.

Mitigation: Use the skill only with data approved for dLazy processing and avoid uploading sensitive or unauthorized audio.

Risk: Voice cloning can be misused when the speaker has not consented.

Mitigation: Clone voices only with the speaker's permission or another clear authorization.

Risk: The dLazy API key may be saved in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include generated output URLs from files.dlazy.com or asynchronous task IDs for later polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
