## Description:

Generate customized speech that highly restores the timbre by uploading reference audio using Kling Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate custom speech through the dLazy Kling Audio Clone CLI by providing reference audio and a name.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference voice audio is uploaded to dLazy media storage for processing.

Mitigation: Use only audio that the user is authorized to upload, and review the dLazy service terms before processing sensitive or regulated voice data.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration or supplied per invocation.

Mitigation: Use a scoped organization key where possible, protect the local config file, and rotate or revoke the key if it is exposed.

Risk: The published examples and output schema appear inconsistent with the audio-cloning command.

Mitigation: Run `dlazy kling-audio-clone -h` and use `--dry-run` when available to confirm required flags and expected output before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-audio-clone)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task IDs or hosted output URLs; confirm the current CLI help before use because evidence flags inconsistent examples and output documentation.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
