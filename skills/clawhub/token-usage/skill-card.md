## Description:

Track, aggregate, and report OpenClaw token usage and costs across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect local OpenClaw and Codex session usage, estimate token costs, compare usage over time, and export reports for budget monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local OpenClaw and Codex session logs and creates aggregate usage data.

Mitigation: Install and run it only where local session metadata may be inspected, and keep generated reports under the same access controls as the source logs.

Risk: JSON exports and Telegram-ready reports may reveal sensitive usage metadata such as dates, models, session categories, and cost estimates.

Mitigation: Review exports before sharing and avoid sending reports to channels that are not approved for operational metadata.

Risk: Documented maintenance commands can compress or move old session files.

Mitigation: Run archive commands only after explicit user approval and after confirming that older session files are no longer needed in place.

Risk: Cost reports are estimates based on pricing data that can become stale.

Mitigation: Refresh or review pricing data before using reports for billing decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/space-cadet/skills/token-usage)
- [Project Homepage](https://github.com/space-cadet/openclaw-tools/tree/main/skills/token-usage)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and terminal reports with optional JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cost estimates depend on the bundled or user-edited pricing data and may differ from actual billing.]

## Skill Version(s):

2.5.1 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
