## Description:

Helps an agent use Deyo to transcribe user-specified media URLs or local audio and video files, with optional cleaned transcripts and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casatwy](https://clawhub.ai/user/casatwy)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with Deyo can request transcription of specific media links or exact local audio/video files, then receive cleaned or raw transcripts, timed captions, or summaries of explicitly selected inputs. The skill also guides authorized installation, status checks, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media URLs and local files are processed by Deyo and transcription consumes account minutes.

Mitigation: Use only inputs the user explicitly identifies and confirm permission to use the existing minute balance before submitting a batch.

Risk: Authentication can store a Deyo API key locally.

Mitigation: Check authentication status first; log in or save a key only with explicit authorization, and never disclose the key.

Risk: Installation or updates can change global software or the active OpenClaw skill.

Mitigation: Show the proposed install or update and require explicit user consent before running it.

## Reference(s):

- [Deyo ClawHub release](https://clawhub.ai/casatwy/skills/deyo)
- [Deyo service](https://deyo.miaobi.fun)
- [Sequential transcription and summary](references/batch.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown guidance; transcript files may be text, SRT, VTT, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cleaned text preserves meaning; raw and timed results remain unchanged. Batch requests may produce per-item summaries and a cited overview.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
