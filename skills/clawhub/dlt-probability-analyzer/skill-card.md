## Description:

Generates entertainment-only China Sports Lottery DLT reports that combine expert-view summaries, number-combination analysis, draw checking, cost controls, and plain-language warnings that lottery picks do not improve expected returns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate DLT entertainment analysis reports, check draw outcomes, compare claimed expert picks with baselines, and explain why lottery play remains negative expected value. It is intended for responsible entertainment and harm reduction, not investment, income, or guaranteed-winning decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Windows automation and persistent monitoring can run with more privilege than a lottery report workflow normally needs.

Mitigation: Prefer manual execution; use SYSTEM scheduled tasks only when unattended Windows automation is required and the operator understands the privilege implications.

Risk: The workflow may write reports, ledgers, health-check files, watchdog state, and backups across local user locations such as the desktop.

Mitigation: Inspect configured paths and generated files before broad deployment, and avoid administrator privileges for normal use.

Risk: The workflow may make outbound requests to lottery, expert, or data sites.

Mitigation: Review network access expectations before installation and use offline or skip-download modes when current network retrieval is not acceptable.

Risk: Lottery analysis can be misread as a winning strategy or financial recommendation.

Mitigation: Keep the entertainment-only warning, negative expected value explanation, and budget guidance visible in agent responses and generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/dlt-probability-analyzer)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)
- [Methodology](artifact/references/methodology.md)
- [Operations](artifact/references/operations.md)
- [FAQ](artifact/references/faq.md)
- [Scripts index](artifact/references/scripts.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and generated local HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local report, ledger, health-check, and backup files; normal use requires only Python 3 standard library.]

## Skill Version(s):

2.1.38 (source: frontmatter, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
