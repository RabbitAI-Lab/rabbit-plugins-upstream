## Description:

Fetches public Kuaishou video search results, creator posts, and video comments through Guaikei, returning structured JSON for trend discovery, competitor monitoring, KOL filtering, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketing teams, MCN operators, market analysts, and developers use this skill to collect public Kuaishou search, post, and comment data for content planning, competitor monitoring, trend analysis, KOL screening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search, profile, or video inputs and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that third-party data flow is acceptable, keep the token in a protected environment variable, and rotate it if exposure is suspected.

Risk: Successful search, post, and comment results are saved to a local logs directory and may contain sensitive business or personal-data records.

Mitigation: Store logs on protected machines, avoid sharing raw exports unnecessarily, and delete logs when they are no longer needed.

Risk: The skill is limited to public Kuaishou data and depends on the availability and authorization behavior of the Guaikei API.

Mitigation: Verify that the requested data is public and permitted, handle empty or error JSON statuses without inventing results, and retry or reduce limits when rate limits or transient API errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-trending-video-fetcher)
- [Guaikei Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON results from the CLI scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful task results are saved under the local logs directory by default.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
