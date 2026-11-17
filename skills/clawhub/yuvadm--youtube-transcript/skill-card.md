## Description:

Fetch and save YouTube video transcripts as clean plain text. Use when the user provides a YouTube URL or wants to extract a transcript from a podcast, interview, or talk.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuvadm](https://clawhub.ai/user/yuvadm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch a YouTube video's subtitles with yt-dlp, clean the VTT cues, and return or save a plain-text transcript for review or summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-supplied YouTube URLs trigger network fetching through yt-dlp.

Mitigation: Use trusted YouTube URLs and add URL allowlisting before treating the skill as low risk.

Risk: User-controlled output paths can write outside the intended transcript location.

Mitigation: Prefer stdout or constrain file writes to a dedicated transcript directory with validated filenames.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuvadm/skills/youtube-transcript)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Guidance]

**Output Format:** [Plain text transcript, optionally saved to a file, with markdown guidance for command usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a YouTube URL, optional subtitle language code, and optional output file path.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
