## Description:

大乐透一站看 helps agents generate entertainment-only Super Lotto reports that combine expert-view aggregation, number-picking references, draw-result checks, cost-structure calculations, randomness tests, and responsible-use warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External users and agents use this skill to create transparent, entertainment-only China Sports Lottery Super Lotto analysis reports, compare expert claims with random baselines, check draw outcomes, and keep spending expectations realistic. It is not a betting, investment, or positive-return system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches public lottery data and writes reports, ledger files, and history files on the local machine.

Mitigation: Install only if local file creation and public-data network access are acceptable, and review generated files before relying on them.

Risk: The artifact includes Windows batch files and scheduled-task guidance that can create persistent background automation.

Mitigation: Do not run batch files, admin PowerShell, or schtasks commands unless persistent scheduled execution is explicitly desired.

Risk: Generated number combinations could be misread as financial or betting advice.

Mitigation: Treat all numbers and reports as entertainment only; do not use them as evidence of improved odds, positive return, investment value, or budget decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/dlt-probability-analyzer)
- [README](README.md)
- [FAQ](references/faq.md)
- [Methodology](references/methodology.md)
- [Operations](references/operations.md)
- [Script Index](references/scripts.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated local HTML/JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports must frame lottery numbers as entertainment, not financial advice or improved odds.]

## Skill Version(s):

2.1.37 (source: frontmatter, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
