## Description:

Calculates structured DCA, exchange-rate, and portfolio-diagnosis reports from user-provided index, holding-cost, available-cash, and exchange-rate inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[987618350-cmd](https://clawhub.ai/user/987618350-cmd)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to turn their own investment, portfolio, and exchange-rate inputs into structured calculation reports for DCA timing, exchange planning, and holding diagnosis. Outputs should be reviewed as decision support, not financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill provides action-oriented investment and exchange decision support.

Mitigation: Treat outputs as calculations and prompts for user review, not as financial advice or instructions to transact.

Risk: Broad finance-related activation terms may trigger the skill unexpectedly in general conversation.

Mitigation: Confirm that the user wants DCA, exchange-rate, or portfolio-diagnosis support before producing an operation-oriented report.

Risk: Financial outputs can be misleading when required user data is missing or stale.

Mitigation: Require current point level, yearly high, holding cost, available funds, and relevant exchange-rate data before producing a recommendation-style calculation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/987618350-cmd/skills/dca-decision-calculator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown-like structured reports with calculations and risk warnings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided market, portfolio, cash, and exchange-rate inputs; caps single DCA multiplier at 5x.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
