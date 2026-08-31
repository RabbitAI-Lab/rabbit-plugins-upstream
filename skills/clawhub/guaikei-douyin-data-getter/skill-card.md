## Description:

Helps agents collect public Douyin search results, creator posts, comments, and trending-topic data for content research, competitor analysis, sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content teams use this skill to run Douyin public-data collection workflows for market research, competitor monitoring, comment analysis, and trend discovery. The skill maps natural-language research requests to Node.js CLI commands that return structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to run for short-video or competitor-analysis requests that do not explicitly mention Douyin.

Mitigation: Confirm the user intends Douyin public-data collection before running commands or sending queries to the API.

Risk: Search terms, account URLs, and video URLs are sent to a third-party API service.

Mitigation: Avoid sensitive research terms, private URLs, or confidential campaign details unless third-party processing is acceptable.

Risk: Fetched results are saved as local JSON logs and may include bulk comment or account data.

Mitigation: Treat generated logs as reviewable data exports, apply privacy and platform-policy checks, and remove logs when retention is not needed.

Risk: Returned data may expose media-related fields even though downloading is out of scope.

Mitigation: Use returned data for analysis only; do not download, rehost, or redistribute media unless separately authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-getter)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Input and output JSON schemas](assets/*.schema.json)
- [Guaikei token and usage documentation](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Structured JSON on stdout with timestamped JSON result logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; supports keyword, creator post, comment, and hot-list collection; single requests can return up to 10000 items.]

## Skill Version(s):

1.0.0 (source: package.json, references/changelog.md, artifact constants, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
