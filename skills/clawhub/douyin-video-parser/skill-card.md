## Description:

Parses a user-provided Douyin short or long video link, downloads the video, transcribes it locally with faster-whisper, and produces Chinese transcript files plus an interactive HTML analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouq2039-lang](https://clawhub.ai/user/zhouq2039-lang)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to turn Douyin videos into readable Chinese transcripts and structured content analysis. It is intended for workflows that need to inspect, summarize, and reuse short-video content without API keys or cloud transcription services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads Douyin media and writes transcript and report files locally.

Mitigation: Use explicit links, avoid private or sensitive videos when logs or output directories are retained, and review generated local files before sharing.

Risk: The full plain transcript is printed into the terminal or agent session.

Mitigation: Run in a session where logs are appropriately retained or redacted, especially for sensitive video content.

Risk: Running the skill can install faster-whisper and cache a model locally.

Mitigation: Install dependencies in an approved environment and account for the local model cache before deployment.

Risk: Processing untrusted or malformed links can trigger network requests and local file writes.

Mitigation: Prefer sandboxed execution for untrusted links and review the resolved link before running the downloader.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhouq2039-lang/skills/douyin-video-parser)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text transcript files, terminal transcript text, and a single-file HTML analysis report; agent-facing follow-up analysis is Markdown-style prose.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes timestamped and plain transcript files plus an HTML report under the configured output directory; prints the full plain transcript into the terminal/session.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter and skill.yaml report 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
