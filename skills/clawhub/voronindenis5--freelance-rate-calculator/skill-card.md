## Description:

Calculates sustainable freelance or contract rates and fixed-bid project prices using taxes, unpaid non-billable time, bench months, self-funded benefits, and overhead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External freelancers, consultants, developers, and designers use this skill to estimate sustainable hourly rates, evaluate offered contract rates, and price fixed-bid projects. It is a planning aid, not tax or financial advice.

### Deployment Geography for Use:

Global, with US-tax defaults that users should adjust for other jurisdictions.

## Known Risks and Mitigations:

Risk: US-centric tax defaults can produce misleading estimates for other jurisdictions or unusual tax situations.

Mitigation: Adjust the tax inputs for the user's location and circumstances, and treat the results as estimates rather than professional tax advice.

Risk: Freelance pricing outputs can be misleading when target income, overhead, benefits, billable ratio, or bench assumptions are unrealistic.

Mitigation: Review the assumptions before using a quote, compare them against actual costs and pipeline data, and rerun the calculator when assumptions change.

## Reference(s):

- [Rate Theory](references/rate-theory.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and terminal text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline Python stdlib calculator; assumptions are configurable through command-line flags.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
