## Description:

Piper TTS helps an agent generate local text-to-speech voice messages with Piper and return the resulting audio path for supported channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they want an agent to create on-demand local TTS voice messages from provided text. It is intended for explicit local TTS requests that may involve setup commands, voice model downloads, and generated MP3 files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary reports vague trigger rules and missing referenced shell scripts, creating risk of unintended or uninspectable command execution.

Mitigation: Review the skill before installation and only allow setup or speech-generation commands after verifying the exact script files being executed.

Risk: Completing setup may install local packages, download voice models, and create MP3 files.

Mitigation: Run setup only in an approved local environment and confirm storage, network, and package-installation expectations before execution.

## Reference(s):

- [Piper Voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and voice media path markup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local MP3 files after setup and speech generation commands are run.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
