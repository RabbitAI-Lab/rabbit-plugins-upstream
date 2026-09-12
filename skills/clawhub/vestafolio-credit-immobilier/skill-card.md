## Description:

Compute French mortgage monthly payments (insurance included), total interest and the full amortization schedule using Vestafolio's simulator API, after asking the simulator's questions (amount borrowed, annual rate, duration, insurance rate).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to estimate fixed-rate French mortgage payments, insurance cost, total interest, and month-by-month amortization schedules. It is intended for mortgage payment and loan-cost questions, not borrowing-capacity, buy-versus-rent, or notary-fee calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Loan amount, annual rate, duration, and insurance rate are sent to Vestafolio's external API for calculation.

Mitigation: Before the API call, explain the destination, summarize the exact fields and values to be sent, obtain user agreement, and omit unnecessary identifiers, credentials, files, and conversation history.

Risk: Mortgage estimates may be mistaken for a loan offer or financial advice.

Mitigation: State that results are estimates, identify modeled assumptions and omitted costs such as fees and guarantees, and clarify that the response is not financial advice.

## Reference(s):

- [Vestafolio Credit Immobilier API](https://www.vestafolio.com/api/tools/v1/credit-immobilier)
- [Vestafolio Credit Immobilier Simulator](https://www.vestafolio.com/simulateurs/credit-immobilier)
- [ClawHub Skill Page](https://clawhub.ai/vestafolio/skills/vestafolio-credit-immobilier)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text with mortgage figures, assumptions, limitations, and amortization-table details when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are grounded in the Vestafolio API response after the user provides required loan parameters and consents to the external API call.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
