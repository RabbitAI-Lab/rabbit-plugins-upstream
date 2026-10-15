## Description:

Retrieves public Kuaishou videos, creator posts, and comments to support demand research, content monitoring, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketing teams, and analysts use the skill to search public Kuaishou videos, inspect creator posts, and collect comments for trend research and evidence-backed demand analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested keywords, Kuaishou URLs, query limits, and the GUAIKEI API token are sent to the third-party service.

Mitigation: Use only when that data transfer is acceptable; safeguard the API token and avoid sensitive queries.

Risk: Local logs retain collected comments and other research results.

Mitigation: Review and delete logs when the task is complete, especially after large comment collections.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-demand-mining)
- [GUAIKEI service](https://www.guaikei.com)
- [Options and examples](references/options.md)
- [Demand mining workflow](references/demand-mining.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries with structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns status and error details; task results are also saved in local logs.]

## Skill Version(s):

1.0.0 (source: server release, skill frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
