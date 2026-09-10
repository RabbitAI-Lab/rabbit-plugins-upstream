## Description:

Helps agents retrieve public Kuaishou search results, creator videos, and video comments for content research, topic planning, competitive comparison, trend review, and material collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content operators, brand researchers, creators, and data analysts use this skill to collect structured public Kuaishou video, creator, and comment data for research, reporting, trend analysis, and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, profile or video URLs, requested limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run the skill only where use of the third-party API is approved, and provide tokens through controlled environment variables.

Risk: Fetched public comments and account or video metadata are saved locally under the skill logs directory.

Mitigation: Delete generated log files when they are no longer needed and avoid storing or sharing collected data outside authorized research workflows.

Risk: Collected public platform data can be misused outside compliant research, marketing, or reporting workflows.

Mitigation: Limit use to authorized public-data analysis and review downstream summaries or reports for legal, platform, and privacy compliance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-search-comment-creator-fetcher)
- [Guaikei API Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; command results are status-bearing JSON and successful results are also saved as local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command outputs include request metadata, status, error_code, message, timestamp, skill metadata, and results.]

## Skill Version(s):

1.0.0 (source: release evidence, package.json, frontmatter, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
