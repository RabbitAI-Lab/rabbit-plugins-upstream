## Description:

bili-review helps agents summarize Bilibili videos by fetching AI subtitles and comment threads for LLM analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frozentearz](https://clawhub.ai/user/frozentearz)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to turn a Bilibili video URL or BV identifier into subtitle text, popular comments, and structured material for a concise video and comment-section summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local browser cookies for Bilibili and store a reusable cookies.txt file.

Mitigation: Install only when that behavior is acceptable; prefer a dedicated browser profile or low-risk account and delete cookies.txt after use.

Risk: Subtitle and all workflows may require login state and can trigger automatic cookie extraction when no valid cookies.txt exists.

Mitigation: Require confirmation before running login, subtitle, or all workflows that need login state, especially on shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frozentearz/skills/bili-review)
- [Publisher profile](https://clawhub.ai/user/frozentearz)
- [Project homepage](https://github.com/frozentearz/bili-review)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and plain text video metadata, subtitles, comments, and suggested summary structure.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and yt-dlp; subtitle workflows may use browser-derived Bilibili cookies.]

## Skill Version(s):

1.2.3 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
