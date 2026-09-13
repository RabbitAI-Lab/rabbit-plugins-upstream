## Description:

Searches Kuaishou public videos by keyword, lists public creator posts, and collects public video comments through the Guaikei API for content research and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, MCN operators, and analysts use this skill to research public Kuaishou trends, monitor competitor creators, identify KOLs, and collect comments for downstream summaries or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, creator URLs, or video URLs are sent to guaikei.com with a GUAIKEI_API_TOKEN.

Mitigation: Use only when sharing those public-data queries with the Guaikei service is acceptable, and keep the API token scoped and protected.

Risk: Returned public-data JSON is stored locally in logs and may contain sensitive research context.

Mitigation: Review and delete logs on shared machines or when research topics are sensitive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/kuaishou-guaikei-content-research)
- [Guaikei API access](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and writes returned public-data JSON to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
