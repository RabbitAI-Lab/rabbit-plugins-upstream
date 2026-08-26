## Description:

Summarizes Bilibili videos by combining AI subtitles, danmaku timing, and comment-thread analysis into a structured Markdown report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frozentearz](https://clawhub.ai/user/frozentearz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to analyze Bilibili videos, extracting subtitles, danmaku timing signals, and nested comment evidence for concise research-style summaries and action guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can extract and reuse Bilibili-related browser session cookies stored in cookies.txt.

Mitigation: Run the explicit login command yourself, inspect or delete cookies.txt after use, and avoid shared or untrusted workspaces.

Risk: Local cookie files may be readable by other users or tools if the workspace or filesystem permissions are not controlled.

Mitigation: Use the skill only in a private local environment and verify that generated cookie files remain restricted to the current user.

Risk: ClawScan marked the release suspicious because of cookie extraction and reuse behavior.

Mitigation: Review the included scripts and install only if that cookie-handling behavior is acceptable for the intended environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frozentearz/skills/bili-review)
- [Project homepage](https://github.com/frozentearz/bili-review)
- [Interactive flowchart](https://frozentearz.github.io/bili-review/flowchart.html)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with optional tables, checklists, and Mermaid diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local Python scripts and yt-dlp to fetch Bilibili subtitles, danmaku, and comments.]

## Skill Version(s):

2.1.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
