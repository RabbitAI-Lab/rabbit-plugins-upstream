## Description:

Retrieves public Xiaohongshu note search results, note details, comments, and creator post lists to support content, competitor, KOL, and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, content operators, analysts, and agents use this skill to run command-line Xiaohongshu public-data lookups for keyword research, note and comment review, creator monitoring, competitor analysis, and trend discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, full Xiaohongshu note or profile links, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable, scope tokens appropriately, and avoid private, login-only, or session-specific links.

Risk: Command results are saved locally and may contain sensitive business, marketing, or personal-data records.

Mitigation: Restrict access to generated logs and delete them when they are no longer needed.

Risk: The skill is intended for public Xiaohongshu data and can return empty or error statuses when inputs are invalid, unavailable, rate-limited, or inaccessible.

Mitigation: Check the structured status and error_code fields before summarizing results, and do not infer missing data from empty or failed responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-search-and-detail)
- [guaikei API service](https://www.guaikei.com)
- [Options and invocation guide](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; CLI execution returns structured JSON and writes local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands accept keyword, Xiaohongshu note URL, profile URL, short URL, filtering, sorting, time range, and limit options.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
