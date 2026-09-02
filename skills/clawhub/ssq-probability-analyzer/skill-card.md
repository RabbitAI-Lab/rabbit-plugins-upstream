## Description:

双色球一站看 produces responsible-play lottery analysis reports, entertainment-only number combinations, draw checks, randomness tests, and method debunking for China's Double Color Ball lottery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate entertainment-only Double Color Ball analysis, check draw results, compare expert picks, and understand why lottery prediction methods do not provide a positive expected return. It is intended for responsible-play education and report generation, not as investment, betting, or guaranteed-winning advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write HTML, JSON, and cache files locally and copy reports outside the workspace.

Mitigation: Review output locations before installation and run manually when possible so generated files are expected and inspectable.

Risk: The skill describes background automation, scheduled execution, watchdog behavior, and elevated Windows setup paths.

Mitigation: Do not enable WorkBuddy automation, Windows Scheduled Task, SYSTEM/admin setup, watchdog, or localhost state service unless recurring background behavior is explicitly desired and disablement steps are understood.

Risk: The skill uses live network data for lottery reports.

Mitigation: Use offline or skip-download mode when live data is unnecessary, and treat stale or fallback data as entertainment-only context.

Risk: Lottery analysis can be misused as betting or financial guidance.

Mitigation: Preserve the skill's responsible-play framing: no guaranteed results, no positive expected return, and no use as investment, borrowing, or recovery advice.

## Reference(s):

- [Methodology and Mathematical Basis](references/methodology.md)
- [Responsible Play Guidance](references/responsible_play_2026.md)
- [Operations and Safeguards](references/operations.md)
- [Script Index](references/scripts.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated local HTML/JSON report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are entertainment-only and should preserve responsible-play warnings, negative expected value, and no-guarantee statements.]

## Skill Version(s):

2.1.48 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
