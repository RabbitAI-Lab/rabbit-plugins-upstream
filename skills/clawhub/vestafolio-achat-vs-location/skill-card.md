## Description:

Compare final net wealth between buying a primary residence with a mortgage and renting while investing savings, over a chosen horizon, using Vestafolio's simulator API, after asking the simulator's questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and assistant agents use this skill to compare buying a primary residence in France against renting while investing available savings. It helps gather required assumptions, call Vestafolio's simulator API, and explain estimated net wealth, break-even timing, and recommendation drivers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may transmit user-supplied rent-versus-buy assumptions and savings figures to Vestafolio's API.

Mitigation: Tell users before calling the API when sensitive financial assumptions will be sent to Vestafolio, and avoid collecting unnecessary personal data.

Risk: The simulator output can be mistaken for financial advice or a complete cost model.

Mitigation: Present results as estimates, state assumptions and omitted costs, and avoid treating the recommendation as personalized financial advice.

## Reference(s):

- [Vestafolio achat-vs-location API](https://www.vestafolio.com/api/tools/v1/achat-vs-location)
- [Vestafolio achat-vs-location simulator](https://www.vestafolio.com/simulateurs/achat-vs-location)
- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-achat-vs-location)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Markdown guidance with API request examples and user-facing simulation summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires complete user assumptions and network access to Vestafolio's API; outputs are estimates, not financial advice.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
