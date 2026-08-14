## Description:

Downloads a user-provided short-video link, transcribes it locally with faster-whisper, guides caller-side AI analysis, and generates an interactive capsule-card HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and analysts use this skill to break down a single explicit video link into a local transcript, structured analysis JSON, and a shareable HTML report. It is suited for content review workflows where the caller controls the input URL and output directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads video content from user-provided URLs and can use a cookies file for platform authentication.

Mitigation: Run it only on explicit, trusted URLs, confirm you have rights to process the content, and provide cookies only when intentionally granting logged-in access.

Risk: Transcripts, analysis JSON, and HTML reports may contain personal or sensitive information and are written to the local output directory.

Mitigation: Use an output directory you control, avoid private or sensitive videos unless approved, and review generated files before sharing them.

Risk: The first run may download and cache a Whisper model of about 500 MB.

Mitigation: Allow the model download only in approved environments and account for network and storage use before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/hot-video-breakdown)
- [Publisher profile](https://clawhub.ai/user/zhouq2039-lang)

## Skill Output:

**Output Type(s):** [Text, JSON, HTML, Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated transcript text, analysis JSON, and local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires one user-provided video link per run; may download a Whisper model on first use and writes outputs under the configured output directory.]

## Skill Version(s):

1.0.2 (source: frontmatter, skill.yaml, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
