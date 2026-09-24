## Description:

Reduce noise, hiss, and static in a speech recording with Yaps. Save a separate clean file. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to clean speech recordings with the local Yaps desktop engine while preserving the source recording and saving a separate cleaned audio file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as an audio cleaner but includes a broader Yaps CLI adapter for media and account-related workflows.

Mitigation: Review the requested Yaps command scope before execution and use only the audio cleaning workflow needed for the task.

Risk: The workflow depends on a local Yaps desktop or CLI session and may require account readiness or model downloads.

Mitigation: Keep Yaps updated, confirm any model download before approving it, and do not approve unexpected Keychain prompts or account reconnection requests.

Risk: Audio processing can overwrite or replace user files if unsafe output paths are used.

Mitigation: Write cleaned audio to a separate output path, preserve the source file, and require explicit permission before any overwrite.

## Reference(s):

- [Runtime Guide](references/runtime.md)
- [Yaps Download](https://yaps.ai/download)
- [ClawHub Skill Page](https://clawhub.ai/yaps/skills/yaps-audio-cleaner)
- [Publisher Profile](https://clawhub.ai/user/yaps)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and links to cleaned audio files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include processing metrics, quality limitations, and file validation notes.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
