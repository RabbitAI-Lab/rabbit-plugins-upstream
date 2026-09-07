## Description:

Helps agents compute French income tax with Vestafolio's simulator API after collecting the required income and household inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer French resident income-tax questions by collecting simulator inputs, calling Vestafolio's API, and grounding the response in returned tax figures.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Sensitive income and household details are sent to Vestafolio's third-party API.

Mitigation: Ask only for the required simulator inputs, avoid names, tax identifiers, addresses, account numbers, and unrelated personal details, and make clear that the data is sent to Vestafolio's API before submission.

Risk: A tax answer may be treated as definitive advice even though the skill is grounded in a simulator and the modeled rules can change.

Mitigation: State that results are estimates, ground numerical answers in successful API responses, include relevant assumptions and exclusions, and link the interactive simulator.

## Reference(s):

- [Vestafolio income tax simulator](https://www.vestafolio.com/simulateurs/impot-revenu)
- [Vestafolio income tax API schema](https://www.vestafolio.com/api/tools/v1/impot-revenu)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with API-grounded tax figures and occasional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should be in French when the user writes in French and should state assumptions, limits, and simulator/API grounding.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
