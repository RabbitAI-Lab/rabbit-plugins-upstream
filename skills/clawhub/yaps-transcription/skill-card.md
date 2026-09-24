## Description:

Turn an audio or video file into text with Yaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yaps](https://clawhub.ai/user/yaps)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, developers, and agents use this skill to transcribe local audio or video files into text with the Yaps desktop engine, including interviews, podcasts, and voice memos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local media files through Yaps and the agent host.

Mitigation: Use it only with media files that may be processed by the local Yaps desktop engine and the active agent host.

Risk: Optional transcription features may require model or dependency downloads.

Mitigation: Inspect the installed feature list and authorize downloads only after reviewing the reported size.

Risk: Meeting workflows may leave projects or audio in Yaps-managed storage.

Mitigation: Review and manage retained meeting projects inside Yaps when using speaker-label workflows.

Risk: Unexpected credential prompts or account setup requests could expose account risk.

Mitigation: Do not approve unexpected Keychain prompts or create a separate plugin account; sign in and manage access inside Yaps.

## Reference(s):

- [Running Yaps from a local agent](references/runtime.md)
- [Download or open Yaps](https://yaps.ai/download)
- [ClawHub skill page](https://clawhub.ai/yaps/skills/yaps-transcription)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, Files]

**Output Format:** [Plain text transcript files with concise Markdown status responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports output path, engine, duration, and word count; transcript contents are read only when requested.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
