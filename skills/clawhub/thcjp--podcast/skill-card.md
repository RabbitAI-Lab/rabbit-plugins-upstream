## Description:

播客 helps agents plan podcast episodes, draft scripts and show notes, suggest audio and video production settings, identify social-media clips, and prepare distribution guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, and developers use this skill to plan and grow podcasts, draft episode scripts and show notes, and prepare audio, video, clipping, and SEO guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted transcription, LLM, or media services may receive audio, transcripts, file names, and prompts.

Mitigation: Use local-only processing where required and review service privacy terms before sending media or transcripts to external services.

Risk: API keys or service credentials may be exposed if placed in prompts, files, logs, or version control.

Mitigation: Store credentials in environment variables and avoid including secrets in prompts or committed files.

Risk: Processing copyrighted or sensitive recordings can create privacy, consent, or copyright issues.

Mitigation: Use original or properly licensed media, obtain consent for sensitive recordings, and avoid processing copyrighted media without permission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/podcast)
- [FFmpeg downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces planning, script, show-note, clip, and media-processing recommendations; actual media editing depends on external tools.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
