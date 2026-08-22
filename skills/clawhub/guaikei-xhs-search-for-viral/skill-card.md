## Description:

Provides structured public Xiaohongshu data for viral-note discovery, competitor monitoring, KOL screening, note details, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand marketers, data analysts, MCN teams, and operations teams use this skill to retrieve public Xiaohongshu notes, creator posts, note details, and comments for content planning, competitive monitoring, KOL screening, and trend research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs and the GUAIKEI API token to the guaikei.com service.

Mitigation: Use only approved public-data queries, keep the API token scoped and protected, and avoid submitting sensitive business research unless this data flow is acceptable.

Risk: Each run may save full JSON results locally in logs/.

Mitigation: Protect or delete generated log files when they contain sensitive research terms, comments, profile links, or xsec_token URLs.

Risk: The skill is intended for public Xiaohongshu data and does not support private, hidden, or login-only content.

Mitigation: Confirm requested data is public and authorized before running the CLI commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-for-viral)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result handling]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs Node.js CLI commands that retrieve structured JSON and save full results locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
