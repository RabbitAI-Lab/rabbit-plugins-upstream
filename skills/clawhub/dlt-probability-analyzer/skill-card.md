## Description:

大乐透一站看 helps agents generate entertainment-only China Sports Lottery Super Lotto reports, compare public expert picks, check draw results, and explain why lottery picks do not improve odds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to run a local Python workflow for entertainment-only DLT number reports, draw checking, budget-aware lottery education, and anti-scam explanations. It is not for investment, profit, or guaranteed winning claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local Python scripts, fetch public lottery data, write report and ledger files locally, and interact with Windows scheduling workflows.

Mitigation: Install only with explicit consent, prefer the on-demand run_dlt.py path, and review scheduled-task XML, restore inputs, and integrity-baseline behavior before enabling background automation.

Risk: Lottery reports can be mistaken for financial advice, profit claims, or a way to improve winning odds.

Mitigation: Keep entertainment-only, no-advantage, and budget-limit warnings in agent responses and generated reports; reject requests for guaranteed wins, positive expected returns, or betting escalation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/dlt-probability-analyzer)
- [README](README.md)
- [Methodology and mathematical basis](references/methodology.md)
- [Operations and health checks](references/operations.md)
- [Script index](references/scripts.md)
- [FAQ](references/faq.md)
- [2026 web research and responsibility notes](references/web_research_2026.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands and generated local HTML/JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch public lottery data and write local report, ledger, history, and health-check files.]

## Skill Version(s):

2.1.46 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
