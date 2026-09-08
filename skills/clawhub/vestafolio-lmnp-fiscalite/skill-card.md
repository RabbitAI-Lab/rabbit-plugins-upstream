## Description:

Compare LMNP furnished-rental taxation between micro-BIC and regime reel with amortization using Vestafolio's simulator API after collecting the simulator's required inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect LMNP furnished-rental facts, call Vestafolio's simulator, and compare micro-BIC against regime reel for French rental-tax planning. It is suited to guidance and estimate workflows, not a substitute for professional tax advice.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: User-provided rental, tax-rate, purchase-price, financing, and expense values may be sent to Vestafolio's API for calculation.

Mitigation: Avoid unnecessary identifying details and review Vestafolio's privacy terms before entering sensitive financial data.

Risk: Simulator results are estimates based on the rules coded in the tool and may not reflect future finance-law changes or individual tax advice needs.

Mitigation: State assumptions and limits with the result, link the interactive simulator, and recommend professional tax review for filing or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-lmnp-fiscalite)
- [Vestafolio LMNP fiscalite simulator](https://www.vestafolio.com/simulateurs/lmnp-fiscalite)
- [Vestafolio LMNP fiscalite API schema](https://www.vestafolio.com/api/tools/v1/lmnp-fiscalite)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain text with concise explanation and simulator-backed numeric results when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounds personalized recommendations in Vestafolio API results and reports inability to compute when execution or network access is unavailable.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
