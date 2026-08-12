## Description:

Parses Bilibili video URLs to extract metadata, download and merge media streams, analyze visual frames with VLM, and transcribe speech with ASR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers, agents, and external users use this skill to turn a Bilibili video URL into a structured content report with public metadata, optional subtitles, sampled visual analysis, audio transcription, and synthesized findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video frames and audio chunks may be sent to the external AI provider configured for the z-ai CLI.

Mitigation: Use --skip-visual or --skip-audio for sensitive videos, and review the configured provider's terms before processing private, confidential, or rights-restricted content.

Risk: The skill downloads Bilibili media and writes temporary media, frame, audio, and transcript files in the selected work directory.

Mitigation: Use trusted work directories, avoid untrusted media or subtitle URLs, and keep temporary files only when needed for review.

Risk: Bilibili public API and CDN behavior may change or return time-limited stream URLs.

Mitigation: Re-fetch stream URLs close to processing time and review failures before relying on generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/bilibili-video-parser-2)
- [Skill workflow documentation](artifact/skill.md)
- [README](artifact/README.md)
- [Bilibili view API example](https://api.bilibili.com/x/web-interface/view?bvid=BV1q2RhB9EQC)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis, Shell commands, Guidance]

**Output Format:** [Structured JSON with metadata, visual-analysis entries, transcript text, and summary fields; guidance may be provided as Markdown with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The parser can write results to an output file and can skip download, visual analysis, or audio transcription through command-line flags.]

## Skill Version(s):

0.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
