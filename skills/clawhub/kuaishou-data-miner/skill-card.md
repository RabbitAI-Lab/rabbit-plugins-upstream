## Description:

Retrieves public Kuaishou data for keyword video search, creator post monitoring, and video comment collection, returning structured data for topic research, competitor monitoring, KOL screening, comment analysis, and trend insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketing teams, analysts, and agents use this skill to collect public Kuaishou search results, creator posts, and video comments for downstream analysis or reporting. It is suited to content ideation, competitor analysis, creator tracking, and comment sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms, profile or video URLs, and the GUAIKEI_API_TOKEN are sent to the guaikei.com API.

Mitigation: Use the skill only when that third-party API use is acceptable for the target data and environment.

Risk: Result logs may retain competitor research, user comments, or other sensitive analysis outputs on disk.

Mitigation: Review or delete generated logs after use when retained results are not desired.

Risk: The skill retrieves public data only and does not support private, hidden, or login-gated Kuaishou data.

Mitigation: Keep requests limited to public Kuaishou content and avoid asking the skill to bypass access controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/kuaishou-data-miner)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Analysis, Guidance]

**Output Format:** [Structured JSON with status, request metadata, skill metadata, and results, optionally summarized in Markdown by the calling agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs can save result JSON files under logs/; failed or empty runs return structured error JSON.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
