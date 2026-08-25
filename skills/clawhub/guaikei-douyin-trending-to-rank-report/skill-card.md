## Description:

This skill helps agents search Douyin keywords, collect creator posts and video comments, and query real-time hot lists for short-video research, competitor analysis, comment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content researchers, and developers use this skill to run API-backed Douyin public-data collection workflows and receive structured JSON for content planning, competitor analysis, comment review, and trend reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to be selected for ambiguous trend or competitor-research requests.

Mitigation: Invoke it only for explicit Douyin public-data collection tasks, and ask for clarification before using it for general trend, competitor, or short-video research.

Risk: API-backed requests can send search terms, Douyin URLs, result limits, and token-authenticated requests to guaikei.com.

Mitigation: Use a scoped GUAIKEI_API_TOKEN from the environment, avoid sensitive research queries, and confirm that sending these inputs to the service is acceptable for the user.

Risk: Collected search, account, and comment data is saved locally as JSON under logs/ by default.

Mitigation: Review, protect, or delete saved logs when they include sensitive research topics or public user/comment data.

Risk: Server security evidence marks the release verdict as suspicious.

Mitigation: Review the skill and its network and logging behavior before installation or deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trending-to-rank-report)
- [Usage documentation](readme.md)
- [Full option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Request and response JSON schemas](assets/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON on stdout, operational logs on stderr, and saved JSON result files under logs/.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and sends token-authenticated Douyin research requests to guaikei.com.]

## Skill Version(s):

1.0.0 (source: release metadata, package.json, changelog, constants.js)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
