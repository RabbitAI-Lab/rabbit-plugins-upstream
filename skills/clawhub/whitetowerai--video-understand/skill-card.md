## Description:

Builds reusable media metadata, word-level transcripts, speech analysis, and evidence-backed video understanding for downstream editing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video editors use this skill to prepare source-timed transcripts, factual summaries, and review artifacts before making editorial decisions in other skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes editing and rendering code beyond its video-understanding description; it can create a final video and update render status.

Mitigation: Review the included scripts before installation and allow rendering only with a trusted, explicitly approved plan.

Risk: Processing copies and analyzes media, writes project and review files, and runs ffmpeg, ffprobe, and faster-whisper.

Mitigation: Run in a project-specific workspace with trusted media and check generated files before downstream use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/whitetowerai/skills/video-understand)
- [Project schema](reference/project-schema.md)
- [Timeline schema](reference/timeline-schema.md)
- [Understanding schema](reference/understanding-schema.md)
- [Understanding example](examples/understanding.example.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Subtitles, Images]

**Output Format:** [Source-timed JSON evidence, Markdown summary, SRT transcript, and JPEG contact sheet]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires validation and human review of timestamps, transcript, and semantic evidence.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
