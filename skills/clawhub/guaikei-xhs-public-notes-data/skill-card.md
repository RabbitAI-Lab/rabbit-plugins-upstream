## Description:

Retrieves public Xiaohongshu note, comment, creator-post, and keyword-search data for social media research through guaikei.com command-line tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, analysts, and agents use this skill to search public Xiaohongshu notes, inspect note details and comments, and monitor creator posts for topic research, competitor analysis, KOL screening, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note URLs, creator-profile URLs, and the guaikei.com API token are sent to a third-party service.

Mitigation: Install and run the skill only when that data sharing is acceptable, and scope API-token access to the intended environment.

Risk: Returned comments, creator-post data, and command results are saved locally as retained public-data records.

Mitigation: Review the saved logs before further sharing and delete them when they are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and does not support private, login-only, publishing, or interaction workflows.

Mitigation: Use it only for public-data retrieval and decline requests for private, hidden, login-gated, or policy-restricted content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-public-notes-data)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [guaikei.com API token service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with shell commands; command output is structured JSON and saved JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands call guaikei.com and write results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact package/frontmatter report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
