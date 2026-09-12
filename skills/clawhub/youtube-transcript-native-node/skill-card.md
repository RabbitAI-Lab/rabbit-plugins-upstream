## Description:

Extract a clean plain-text transcript from existing YouTube captions - native Node.js, zero npm dependencies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jwestburg](https://clawhub.ai/user/jwestburg)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to extract existing captions from a supported single-video YouTube URL for summarization, quote review, search, or structured JSON handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a local yt-dlp binary to access YouTube for user-provided videos.

Mitigation: Use it only when yt-dlp comes from a trusted install path and the user has approved that dependency.

Risk: Private or client-sensitive videos may be inappropriate to access through YouTube and yt-dlp.

Mitigation: Avoid those videos unless the user confirms that access is appropriate.

Risk: Returned titles and captions are third-party content that may be inaccurate or adversarial.

Mitigation: Treat transcript text as data for analysis, not instructions for the agent to follow.

## Reference(s):

- [YouTube Transcript Contract](references/youtube-transcript-contract.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text transcript, timestamped plain text, JSON transcript object, or compact Markdown response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+ and a trusted yt-dlp binary on PATH; extracts existing captions only and does not transcribe audio.]

## Skill Version(s):

1.1.27 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
