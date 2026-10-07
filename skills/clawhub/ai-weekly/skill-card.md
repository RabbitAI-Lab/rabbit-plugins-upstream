## Description:

Generates a searchable AI news report from public RSS feeds, with an optional short Markdown digest and optional publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and content teams use this skill to compile a weekly AI news digest or generate a searchable, single-file HTML report. Optional workflows distribute the report to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional publishing or Feishu delivery can send reports to an unintended destination.

Mitigation: Enable delivery only when intended, and confirm the destination and credentials before publishing.

Risk: Local deployment configuration may contain sensitive credentials.

Mitigation: Prefer environment variables or managed connector authentication, and review configuration files before sharing.

Risk: Installing the scheduler creates a recurring OS-level refresh task.

Mitigation: Run the scheduler installer only if a recurring refresh is desired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Project homepage](https://github.com/Elisabeth15501/ai-weekly)
- [Data sources](artifact/references/data_sources.md)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Text]

**Output Format:** [Single-file HTML report or Markdown news digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [News items link to original sources; unavailable or estimated market data and dated leaderboard snapshots are labeled.]

## Skill Version(s):

4.0.4 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
