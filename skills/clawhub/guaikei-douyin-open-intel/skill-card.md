## Description:

Searches Douyin public data for keyword videos, creator posts, video comments, and real-time hot lists, returning structured JSON for content planning, competitor analysis, and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and developers use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for content planning, competitor research, and public-opinion monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin research queries, target URLs, and a GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use explicit Douyin-specific requests, submit only the data needed for the task, and protect and rotate the API token.

Risk: Broad auto-trigger rules may invoke the skill for implicit short-video research requests.

Mitigation: Confirm the intended Douyin scope before running commands when the user request is ambiguous.

Risk: Results are saved locally under logs by default and may contain sensitive business or personal-data material.

Mitigation: Handle log files as sensitive data, restrict access, and delete them when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-open-intel)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei service site](https://www.guaikei.com)
- [Complete CLI options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [JSON on stdout with status messages on stderr and optional local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; each command can request up to 10000 public-data records.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
