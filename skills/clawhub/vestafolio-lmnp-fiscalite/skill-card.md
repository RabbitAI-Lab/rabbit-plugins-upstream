## Description:

Compare LMNP furnished-rental taxation between micro-BIC and régime réel with amortization using Vestafolio's simulator API, after asking the simulator's questions (furnished or not, rents, type of meublé, purchase price, notary fees, furniture, works, TMI, annual charges).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare French LMNP furnished-rental tax treatment under micro-BIC and régime réel, including amortization, annual savings, 10-year savings, and regime recommendation.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Personalized calculations can transmit financial inputs such as rental income, property costs, charges, and marginal tax rate to Vestafolio.

Mitigation: Require explicit user approval for the Vestafolio destination and data scope before any API call, summarize the fields to be sent, omit unnecessary identifiers, and offer the manual simulator when declined.

Risk: Tax thresholds, abatements, and amortization treatment can change with French finance laws.

Mitigation: Ground numerical recommendations in the current Vestafolio API result, state assumptions and limits, and avoid presenting the output as tax advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-lmnp-fiscalite)
- [Vestafolio LMNP simulator](https://www.vestafolio.com/simulateurs/lmnp-fiscalite)
- [Vestafolio LMNP API schema](https://www.vestafolio.com/api/tools/v1/lmnp-fiscalite)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown guidance with API-derived calculation results and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return regime comparison, tax amounts, net income, annual and 10-year savings, assumptions, limitations, and links for manual simulation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
