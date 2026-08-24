## Description:

Analyzes GitHub repository releases and summarizes release notes for manual review or cron-driven incremental tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stoner-byte](https://clawhub.ai/user/stoner-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use this skill to inspect the latest or newly published GitHub releases, summarize release notes, and run cron-style release tracking with local state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts GitHub for repositories requested by the user, so release analysis depends on external GitHub API availability and the selected repository.

Mitigation: Use the skill only for repositories the user intends to inspect, and review fetched release data before relying on the summary.

Risk: Cron mode stores tracking state locally and can reuse a custom state key.

Mitigation: Prefer the default state key or a simple trusted custom key, and use the documented state-root override when containment or cleanup is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stoner-byte/skills/github-release-analyzer)
- [Execution Modes](references/execution-modes.md)
- [State Format](references/state-format.md)
- [Summary Contract](references/summary-contract.md)
- [Output Templates](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and deterministic command output JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual mode returns the rendered release summary; cron mode returns NO_REPLY when no eligible release is available.]

## Skill Version(s):

0.0.5 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
