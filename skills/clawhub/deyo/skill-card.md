## Description:

Deyo helps an agent use the installed Deyo CLI to transcribe one explicitly provided supported URL or one exact local audio/video file path, and to handle Deyo install, status, or troubleshooting requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casatwy](https://clawhub.ai/user/casatwy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route explicit Deyo transcription, installation, status, and troubleshooting requests through the Deyo CLI while preserving consent boundaries for inputs, credentials, updates, billing, and output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A transcription request can upload an explicit local media file or process a supported URL and may consume the user's Deyo minute balance.

Mitigation: Proceed only after the current user explicitly identifies one URL or one exact local file path and understands that full transcription may consume minutes.

Risk: Deyo authentication may involve a saved API key.

Mitigation: Check authentication status first, show only masked key information, and save an API key only when the current user explicitly authorizes login.

Risk: The OpenClaw update flow can change the installed skill version.

Mitigation: Run updates only through the verified OpenClaw flow and only after the user explicitly confirms the latest-version update prompt.

Risk: Transcript output can be written to local files.

Mitigation: Write final output only to an authorized destination and use no-clobber delivery for cleaned .txt files.

## Reference(s):

- [Deyo skill on ClawHub](https://clawhub.ai/casatwy/skills/deyo)
- [Deyo service](https://deyo.miaobi.fun)
- [Deyo API keys](https://deyo.miaobi.fun/me/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Agent guidance with inline shell commands; transcription outputs may be cleaned text, raw text, SRT, VTT, JSON, or verbose JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create final transcript files only after explicit user authorization; cleaned text delivery is constrained to .txt outputs.]

## Skill Version(s):

1.0.12 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
