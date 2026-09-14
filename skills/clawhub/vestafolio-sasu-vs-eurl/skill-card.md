## Description:

Compare SASU and EURL net director income for a French solo entrepreneur using Vestafolio's simulator API after collecting the simulator's required business, tax, dividend, and salary inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to compare SASU versus EURL income outcomes for a French solo entrepreneur. The skill gathers the simulator's required inputs, obtains consent before sharing relevant financial or household tax data with Vestafolio APIs, and returns an estimate grounded in the API result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send financial and household tax inputs to Vestafolio APIs.

Mitigation: Review the destination and field summary before use, and approve the API call only when comfortable sharing that data.

Risk: The simulator output may be mistaken for tax or legal advice.

Mitigation: Present results as estimates, state relevant assumptions and limits, and avoid substituting the skill output for professional advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-sasu-vs-eurl)
- [Vestafolio SASU vs EURL simulator](https://www.vestafolio.com/simulateurs/sasu-vs-eurl)
- [Vestafolio SASU vs EURL API schema](https://www.vestafolio.com/api/tools/v1/sasu-vs-eurl)
- [Vestafolio income tax API schema](https://www.vestafolio.com/api/tools/v1/impot-revenu)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text, Markdown]

**Output Format:** [Markdown or text response grounded in Vestafolio API JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user consent before sending relevant financial or household tax inputs to Vestafolio APIs; output is an estimate, not tax or legal advice.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
