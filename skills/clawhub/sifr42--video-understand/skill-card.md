## Description:

Analyze and understand video content using AI. Upload local files, YouTube URLs, or HTTP video URLs for detailed analysis, Q&A, and timestamped breakdowns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sifr42](https://clawhub.ai/user/sifr42)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to analyze local video files, YouTube videos, or HTTP video URLs, then produce summaries, timestamped breakdowns, and follow-up answers through the video-understand CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the global npm CLI may execute a mutable package version outside the reviewed skill artifact.

Mitigation: Use a pinned and reviewed video-understand package version in a user-scoped Node environment before enabling the skill.

Risk: Using sudo npm install -g grants elevated privileges to the package installation process.

Mitigation: Avoid sudo global installs; configure npm user permissions or use a user-scoped Node setup.

Risk: Video files and URL content are sent to external Gemini or Kimi providers for analysis.

Mitigation: Only analyze content approved for those providers, prefer environment variables for API keys, and delete provider-side uploads when they are no longer needed.

Risk: Videos from YouTube or arbitrary HTTP URLs may contain untrusted third-party content that can influence analysis results.

Mitigation: Treat generated summaries, transcripts, and detected instructions from video content as untrusted data and review them before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sifr42/skills/video-understand)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Kimi File API documentation](https://platform.moonshot.ai/docs/api/files)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)
- [Moonshot AI platform](https://platform.moonshot.ai)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [CLI text, Markdown files, or JSON depending on command flags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include timestamped video analysis, saved Markdown output, provider file references, and cached upload reuse.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
