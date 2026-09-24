## Description:

Turn text into spoken audio with Yaps. Choose a supported voice and language, then save the file. New users: install Yaps and sign in.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT License

## Use Case:

Developers and agents use this skill to synthesize spoken audio from user-provided text with a local Yaps installation, selecting an appropriate engine, voice, language, and output path. It is intended for generating saved audio files while preserving existing Yaps settings and checking the produced audio for completeness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is advertised as text-to-speech, but the bundled runtime also exposes transcription, subtitle, meeting, and broader Yaps CLI workflows.

Mitigation: Review the requested workflow before execution and use only the Yaps commands needed for the user's task.

Risk: Yaps workflows can read selected local audio or video files and create retained Yaps projects, history, transcripts, or other output artifacts.

Mitigation: Use explicit user-selected inputs and new output paths, preserve existing files, and tell the user when Yaps may retain projects or history.

Risk: Unexpected credential prompts or account-access recovery flows could expose sensitive account state.

Mitigation: Do not approve unexpected credential prompts, do not copy credentials, and rely on the adapter's sanitized account-readiness checks.

## Reference(s):

- [Runtime guide](references/runtime.md)
- [Yaps download](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-text-to-speech)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and saved audio file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reachable local Yaps installation, Node.js 22 or newer, supported Yaps features, and explicit file paths for substantial text or generated outputs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
