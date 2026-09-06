## Description:

Searches public Kuaishou data, lists creator posts, and fetches video comments for trend discovery, competitor monitoring, KOL screening, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, analysts, and agent developers use this skill to retrieve public Kuaishou search results, creator post listings, and video comments for content planning, competitor monitoring, reporting, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, creator or video URLs, request limits, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when the third-party API service and token handling are approved for the task, and avoid submitting sensitive research targets.

Risk: Retrieved public results, including comments and account or video metadata, are saved locally under logs.

Mitigation: Review local log retention and sharing practices, and remove records that should not be retained.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/kuai-shou-trend-insights)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON results with concise text or Markdown guidance and shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save retrieved public results under local logs.]

## Skill Version(s):

1.0.0 (source: release metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
