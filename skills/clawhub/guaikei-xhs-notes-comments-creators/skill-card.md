## Description:

Retrieves public Xiaohongshu content data by keyword, note URL, comment thread, or creator profile and returns structured JSON for content research, trend analysis, KOL screening, and marketing reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content, marketing, and data-analysis users use this skill to retrieve public Xiaohongshu notes, comments, note details, and creator posts as structured data. The data supports trend research, competitor monitoring, KOL screening, comment analysis, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note or profile URLs, API token authentication, and returned public-content data are sent to guaikei.com.

Mitigation: Install and run the skill only when that data sharing is acceptable, and avoid submitting sensitive research targets or credentials outside approved environments.

Risk: Returned public-content data and business research may be retained locally in the logs/ directory.

Mitigation: Delete, restrict, or otherwise protect logs/ when queries, comments, creator data, or analysis outputs are sensitive.

Risk: The third-party API can return empty, unauthorized, rate-limited, or server-error responses.

Mitigation: Check the returned status and error_code fields before analysis, reduce limits or retry when appropriate, and do not invent conclusions from empty or error results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-notes-comments-creators)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service website](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands; executed scripts return JSON and save local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; requests are sent to guaikei.com and results are stored under logs/.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
