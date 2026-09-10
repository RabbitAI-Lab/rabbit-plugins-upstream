## Description:

Simulate early retirement (FIRE) financed by invested capital for a French saver using Vestafolio's simulator API, after asking the simulator's questions about current situation, mortgage, target age, complementary income, and lifestyle at retirement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to estimate whether invested savings can support early retirement for a French saver. It gathers required financial inputs, obtains explicit approval before sending them to Vestafolio, and reports the simulator result with assumptions and limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal financial planning inputs such as savings, salary, expenses, mortgage information, age, and retirement assumptions may be sent to Vestafolio's API.

Mitigation: Before calling the API, summarize the fields and values to be sent, obtain explicit user agreement, send only required simulator fields, and offer the manual simulator link if the user declines.

Risk: The simulation can be mistaken for financial advice or a definitive retirement forecast.

Mitigation: Present results as estimates, state the simulator assumptions and limits, and avoid inventing results when execution or network access is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-age-retraite)
- [Vestafolio simulator](https://www.vestafolio.com/simulateurs/age-retraite)
- [Vestafolio age-retraite API schema](https://www.vestafolio.com/api/tools/v1/age-retraite)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown]

**Output Format:** [Markdown summary grounded in Vestafolio API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include simulator links, assumptions, limits, and user-approved API-call summaries.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
