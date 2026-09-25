## Description:

Creates a searchable, filterable AI news website from public RSS feeds or a concise Markdown news briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and developers use this skill to compile a weekly AI news digest from public feeds, with source links and optional model rankings, market charts, publishing, and Feishu delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional publishing and Feishu delivery can distribute a report beyond the local workspace.

Mitigation: Review these workflows before enabling them; start with dry-run or no-push where available.

Risk: Deployment uses GitHub or cloud credentials, and optional scheduling enables recurring background activity.

Mitigation: Use minimally scoped, short-lived tokens, keep generated credential configs out of commits, and install the scheduler only when recurring refresh is intended.

## Reference(s):

- [AI Weekly project homepage (skill metadata)](https://github.com/Elisabeth15501/ai-weekly)
- [AI Weekly on ClawHub](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Data sources](artifact/references/data_sources.md)

## Skill Output:

**Output Type(s):** [HTML, Markdown, Guidance, Shell commands]

**Output Format:** [Single-file HTML news site or Markdown briefing, with optional deployment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [News links identify their sources; unsourced market figures are marked as examples or estimates.]

## Skill Version(s):

4.0.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
