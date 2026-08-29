## Description:

bili-review helps an agent fetch Bilibili AI subtitles, timed danmaku, and nested comments, then produce a cross-checked Markdown video summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frozentearz](https://clawhub.ai/user/frozentearz)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers use this skill to analyze a single Bilibili video from a BV/AV ID or URL and generate a concise summary grounded in subtitles, danmaku timing, and comment discussion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically extracts and stores Bilibili browser login cookies for long-term reuse.

Mitigation: Run it in a contained environment or with a dedicated Bilibili account, and remove the saved cookies.txt file when the skill is no longer needed.

Risk: The skill can send authenticated requests to Bilibili when retrieving video data.

Mitigation: Use only accounts and video inputs you are comfortable using with Bilibili, and review the generated summary before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frozentearz/skills/bili-review)
- [Project homepage](https://github.com/frozentearz/bili-review)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown video summary with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries may include timestamps, comment signals, decision cards, tables, and action recommendations for one Bilibili video.]

## Skill Version(s):

2.2.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
