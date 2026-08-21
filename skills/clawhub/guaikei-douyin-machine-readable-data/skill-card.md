## Description:

This skill helps agents query Douyin public data for keyword search, creator posts, video comments, and trending topics, returning machine-readable JSON for content research and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing teams use this skill to collect structured Douyin public search results, creator post data, comments, and hot-list entries for trend tracking, competitor analysis, content planning, and audience feedback review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger on broad market-research or trend-analysis requests and query Douyin through guaikei.com.

Mitigation: Confirm ambiguous requests before running the skill and scope queries to the user's stated Douyin research goal.

Risk: The skill can collect and store bulk social-media data, including comments, profile references, and media URLs.

Mitigation: Collect only the minimum needed records, treat returned data as sensitive, and review or delete the logs directory regularly.

Risk: Returned Douyin data and media URLs may be subject to platform terms and applicable privacy or data-use laws.

Mitigation: Use results only for lawful, policy-compliant analysis and avoid redistributing raw data unless permitted.

Risk: The skill depends on a private token and a third-party service endpoint.

Mitigation: Store GUAIKEI_API_TOKEN only as an environment variable, stop on authentication errors, and avoid exposing token values in outputs or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-machine-readable-data)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Request and response JSON schemas](assets/*.schema.json)
- [Guaikei service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Files, Guidance]

**Output Format:** [Pure JSON on stdout with logs on stderr and optional saved JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single calls can request up to 10000 records and require GUAIKEI_API_TOKEN.]

## Skill Version(s):

1.0.0 (source: server evidence, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
