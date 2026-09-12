## Description:

Computes French household income tax with the 2026 progressive barème, quotient familial and décote using Vestafolio's simulator API after collecting the required tax inputs and obtaining user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to estimate French income tax, marginal tax rate, effective tax rate, family quotient parts and the tax impact of marriage, PACS or children. The skill is for France-specific income-tax calculations and requires explicit consent before sending limited financial inputs to Vestafolio.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: The skill sends personal financial inputs to Vestafolio's external API for ordinary income-tax estimates.

Mitigation: Before any POST request, explain the destination and exact fields to be sent, obtain explicit user agreement for that data scope, and do not transmit data if the user declines.

Risk: Investment-income and rental-income figures may be rough educational estimates outside the API-backed ordinary income-tax calculation.

Mitigation: Treat those figures as estimates and advise verification with the official simulator or a qualified tax professional.

Risk: Tax rates and rules change with finance laws, and the artifact describes the 2026 barème for 2025 income.

Mitigation: State the applicable assumptions and limits with the result, and avoid inventing a calculation when the API or network is unavailable.

## Reference(s):

- [Vestafolio income-tax API endpoint](https://www.vestafolio.com/api/tools/v1/impot-revenu)
- [Vestafolio income-tax simulator](https://www.vestafolio.com/simulateurs/impot-revenu)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text with API-backed tax results, assumptions and limits.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bracket-by-bracket tax details, number of parts fiscales, quotient familial ceiling, decote, reductions, net tax, marginal rate and effective rate.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter declares 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
