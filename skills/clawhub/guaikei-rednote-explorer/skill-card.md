## Description:

Fetches public Xiaohongshu/Rednote search results, note details, comments, and creator posts as structured data for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and content operators use this skill to collect public Xiaohongshu/Rednote data for content research, competitor monitoring, KOL screening, trend analysis, and comment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and Xiaohongshu URLs, including xsec_token query strings, are sent to guaikei.com with the configured API token.

Mitigation: Use the skill only where that data transfer is acceptable, avoid submitting sensitive URLs, and keep GUAIKEI_API_TOKEN scoped and protected.

Risk: Fetched public data is automatically written to local log files after each run.

Mitigation: Review, retain, or delete the logs directory according to the user's data handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-explorer)
- [Guaikei website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with Node.js shell commands; command execution returns structured JSON and saves local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, URL, sorting, time-range, and limit parameters up to 10000 records.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package.json report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
