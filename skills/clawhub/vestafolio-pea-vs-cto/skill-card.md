## Description:

Compare PEA, CTO, and assurance-vie net-of-tax outcomes for French investors by collecting required inputs, calling Vestafolio's simulator API, and explaining the resulting assumptions, warnings, and recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial-planning agents use this skill to compare French PEA, CTO, and assurance-vie investment envelopes after collecting the simulator's required inputs. It is intended for French tax-resident scenarios and returns API-grounded results with caveats rather than mental arithmetic.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Simulator inputs may reveal financial profile details to Vestafolio.

Mitigation: Ask only for required inputs, disclose that the calculation uses Vestafolio's service, and avoid real values when the user does not want that profile shared.

Risk: Users may over-rely on simulated investment and tax outcomes.

Mitigation: Ground answers in the API result, state assumptions and limits, relay warnings, and present the output as a simulation rather than tax advice.

Risk: Network access or API failure can prevent a completed simulation.

Mitigation: State that the calculation could not be completed and provide the interactive simulator link instead of inventing a result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-pea-vs-cto)
- [Vestafolio PEA vs CTO API schema](https://www.vestafolio.com/api/tools/v1/pea-vs-cto)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/pea-vs-cto)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, API Calls]

**Output Format:** [Markdown or plain text with optional shell command examples and API-derived figures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include French-language responses, assumptions, warnings, simulator links, and financial caveats.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter states 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
