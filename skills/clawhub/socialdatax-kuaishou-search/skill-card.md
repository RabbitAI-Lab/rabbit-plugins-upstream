## Description:

Helps agents research Kuaishou videos through keyword search for content, competitor, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and other users search Kuaishou videos to study topics, competing content, and emerging trends, then summarize results with traceable source details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches an unpinned npm package at runtime while using a SocialDataX API key.

Mitigation: Review the package before use; prefer a version-pinned package or a reviewed, preinstalled MCP/CLI setup, and expose the API key only in trusted environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown research summary with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes content identifiers, authors, and visible engagement counts when available; incomplete results should be identified.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
