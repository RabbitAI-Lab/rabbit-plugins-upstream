## Description:

Kuaishou Guaikei Dashi searches public Kuaishou videos by keyword, retrieves creator public posts and video comments, and returns structured JSON for topic research, competitor monitoring, KOL screening, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, brand marketers, MCN teams, and analysts use this skill to collect public Kuaishou search results, creator post lists, and video comments for content planning, competitor tracking, KOL discovery, trend review, and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, URLs, and GUAIKEI_API_TOKEN are sent to the Guaikei API service.

Mitigation: Confirm the user is comfortable with this data transfer and has configured an appropriate token before running the skill.

Risk: Fetched results are saved locally by default and may include sensitive business intelligence or public personal data from comments.

Mitigation: Protect access to the logs directory, periodically delete unneeded results, and review applicable platform, privacy, and storage obligations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/kuaishou-guaikei-dashi)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs return status, error_code, message, request metadata, skill metadata, and results; result JSON is also saved under the local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
