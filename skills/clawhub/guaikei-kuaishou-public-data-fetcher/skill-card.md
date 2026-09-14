## Description:

Fetches public Kuaishou video search results, creator posts, and video comments through Guaikei and returns structured JSON for content research, competitor monitoring, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, MCN operators, market analysts, and developers use this skill to collect public Kuaishou search results, creator post lists, and video comments for downstream analysis and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, profile or video links, task parameters, and returned public data are sent to guaikei.com and may be written to local logs.

Mitigation: Use only approved public-data queries, manage GUAIKEI_API_TOKEN carefully, and review or delete generated logs when queries or collected public data are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-public-data-fetcher)
- [Guaikei service site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON with status, error_code, request, skill_metadata, and results; agent responses may add concise Markdown summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may write command results to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
