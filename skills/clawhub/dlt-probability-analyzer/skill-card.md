## Description:

大乐透一站看 helps agents generate entertainment-only China Sports Lottery DLT reports with expert-view aggregation, number-pick analysis, draw checking, cost controls, and clear warnings that lottery picks do not improve expected returns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create DLT entertainment reports, compare sourced expert views against random baselines, check draw results, and explain lottery randomness and negative expected value. It is intended for responsible entertainment analysis, not investment, betting advice, or claims of improved odds.

### Deployment Geography for Use:

Global, with China-focused DLT lottery data and sources.

## Known Risks and Mitigations:

Risk: The security review flags broad Windows automation, including SYSTEM scheduling, watchdog and restore flows, cross-profile file writes, and WorkBuddy database inspection.

Mitigation: Review these automation pieces before installation; prefer manual current-user execution and avoid creating the SYSTEM scheduled task unless that operational behavior is required.

Risk: Restore, desktop export, ledger recording, location lookup, and peer synchronization can create local side effects beyond a simple report-generation task.

Mitigation: Disable or constrain those features when they are not needed, and do not run restore with force options on untrusted backups.

Risk: Lottery reports and generated number combinations may be misread as betting advice or odds improvement.

Mitigation: Keep the skill's entertainment-only warnings visible and state that all combinations have the same first-prize probability and negative expected value.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/dlt-probability-analyzer)
- [README](README.md)
- [FAQ](references/faq.md)
- [Methodology and mathematical basis](references/methodology.md)
- [Operations and self-checks](references/operations.md)
- [Scripts reference](references/scripts.md)
- [2026 web research notes](references/web_research_2026.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated local HTML/JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Python scripts and may fetch public lottery data unless run in offline mode.]

## Skill Version(s):

2.1.48 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
