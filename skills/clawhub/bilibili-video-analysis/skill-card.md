## Description:

Helps an agent analyze Bilibili videos from topics, trends, related recommendations, or specific videos by turning transcripts, frames, danmaku, comments, and replies into traceable learning and research results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flan89](https://clawhub.ai/user/flan89)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to research Bilibili videos, summarize tutorials and viewpoints, decode visual presentation, analyze audience feedback, and collect bounded product or market signals when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Bilibili video IDs, search terms, and related public-data requests to Bilibili and may store local caches.

Mitigation: Use it only for data you are comfortable sending to Bilibili, and review or clear local caches according to your environment policy.

Risk: Optional visual and ASR features may require ffmpeg, Python packages, and local ASR models.

Mitigation: Approve setup only after reviewing the setup plan and install these dependencies in an isolated environment.

Risk: Authenticated Bilibili access can expose account context if cookies are provided intentionally.

Mitigation: Avoid providing Bilibili cookies unless authenticated requests are explicitly required and approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/flan89/skills/bilibili-video-analysis)
- [Server-resolved GitHub Repository](https://github.com/flan89/bilibili-video-analysis)
- [GitHub Releases](https://github.com/flan89/bilibili-video-analysis/releases)
- [Architecture](docs/architecture.md)
- [Installation](docs/installation.md)
- [ASR](docs/asr.md)
- [Product Vision](docs/product-vision.md)
- [Task Routing](references/task-routing.md)
- [Data Routing](references/data-routing.md)
- [Discovery Strategy](references/discovery-strategy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with source-grounded findings and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should state coverage limits when Bilibili data, subtitles, comments, danmaku, frames, or local ASR inputs are missing or partial.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
