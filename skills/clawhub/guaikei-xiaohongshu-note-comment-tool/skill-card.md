## Description:

This skill uses GUAIKEI API-backed Node.js commands to retrieve recent Xiaohongshu notes, note details, comments, and public author posts for trend and content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to retrieve public Xiaohongshu notes, comments, and author activity for trend monitoring, competitor research, KOL screening, and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note or profile URLs, and the GUAIKEI API token are sent to a third-party service.

Mitigation: Use the skill only when that data sharing is acceptable and authorized for the user's workflow.

Risk: Returned public data and query context are saved locally in logs.

Mitigation: Treat generated logs as sensitive work artifacts and delete or restrict them when they are no longer needed.

Risk: The workflow could be misused for private, login-only, unauthorized, or sensitive profiling tasks.

Mitigation: Limit use to public Xiaohongshu data and decline requests involving private, non-public, or unauthorized data collection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xiaohongshu-note-comment-tool)
- [GUAIKEI service website](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command results are structured JSON and each execution saves returned data to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
