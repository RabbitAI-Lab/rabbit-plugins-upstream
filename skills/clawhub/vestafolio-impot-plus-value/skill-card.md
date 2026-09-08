## Description:

Helps agents estimate French real-estate capital gains tax by collecting required sale and property details, using Vestafolio's simulator API, and explaining abatements, exemptions, LMNP amortization reintegration, and sell-now-versus-wait outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and advisors use this skill to estimate French real-estate capital gains tax for property sales and compare selling now with waiting one year. It is scoped to French property-sale scenarios modeled by the Vestafolio simulator, not securities, professional sellers, IS companies, or non-French tax situations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property prices, sale and purchase dates, rental or LMNP status, amortization, and fee or work amounts may be sent to Vestafolio's API.

Mitigation: Tell users that these details are sent to Vestafolio for calculation and avoid processing information they are not comfortable sharing with that service.

Risk: Tax rules, rates, and abatement schedules can change, and simulator outputs are estimates rather than tax advice.

Mitigation: Present results as estimates, state assumptions and limits, link the interactive simulator, and recommend professional review for consequential tax decisions.

Risk: A schema request alone or hand calculation could produce unsupported personalized results.

Mitigation: Fetch the schema and POST the user's parameters before giving numerical results; if execution or the API is unavailable, say the calculation could not be completed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-impot-plus-value)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/impot-plus-value)
- [Vestafolio simulator API schema](https://www.vestafolio.com/api/tools/v1/impot-plus-value)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown response with calculation summary, assumptions, tax components, timing guidance, and simulator link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies in French when the user writes in French; numerical answers are grounded in the simulator result when network execution is available.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
