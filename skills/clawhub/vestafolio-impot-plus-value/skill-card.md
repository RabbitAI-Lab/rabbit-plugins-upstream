## Description:

Compute French real-estate capital gains tax (impot sur la plus-value immobiliere) with holding-period abatements using Vestafolio's simulator API, after asking the simulator's questions about prices, dates, residence status, rental or LMNP status, amortization, acquisition fees, and renovation deductions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to estimate French real-estate capital-gains tax for a property sale, including residence exemptions, holding-period abatements, LMNP amortization reintegration, and the potential benefit of waiting one more year before selling. The skill gathers required inputs, requests consent, calls Vestafolio's simulator API, and explains the returned result and assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends property sale inputs, including prices, dates, residence status, rental or LMNP status, amortization, and deduction methods, to Vestafolio's external API.

Mitigation: Explain the destination and fields before transmission, obtain explicit user approval, and omit identifying details, unrelated conversation content, credentials, files, and optional data not needed for the simulation.

Risk: Tax estimates may be misunderstood as definitive tax advice or may become outdated as French tax rules change.

Mitigation: State relevant assumptions and limits, ground calculations in the simulator output, and describe the result as an estimate rather than tax advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-impot-plus-value)
- [Vestafolio simulator API](https://www.vestafolio.com/api/tools/v1/impot-plus-value)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/impot-plus-value)
- [Vestafolio website](https://www.vestafolio.com)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Markdown with concise explanations and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Grounds numerical tax estimates in the external simulator response after explicit user approval; otherwise provides the manual simulator link.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
