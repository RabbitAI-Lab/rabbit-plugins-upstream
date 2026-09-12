## Description:

Compare unfurnished rental taxation between micro-foncier and regime reel with deficit foncier using Vestafolio's simulator API after collecting the required rental, charge, tax-rate, and prior-deficit inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare French unfurnished rental income taxation under micro-foncier and regime reel, including deductible charges, deficit foncier handling, annual savings, and the break-even charge level. The skill is intended for simulator-backed estimates, not tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends rental-tax figures to Vestafolio's external simulator API.

Mitigation: Explain the destination and exact fields first, obtain explicit user approval for the API call, and send only the relevant simulator inputs.

Risk: Simulator results may be mistaken for definitive tax advice.

Mitigation: Present outputs as estimates, state assumptions and limits, and advise professional review when deficit foncier or regime selection has material tax consequences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-micro-foncier-vs-reel)
- [Vestafolio publisher profile](https://clawhub.ai/user/vestafolio)
- [Vestafolio simulator API schema](https://www.vestafolio.com/api/tools/v1/micro-foncier-vs-reel)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/micro-foncier-vs-reel)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Markdown explanation grounded in JSON simulator results, with optional shell commands when an agent needs to call the API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assumptions, limits, recommended tax regime, annual savings, break-even charges, and a simulator link.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
