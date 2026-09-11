## Description:

Determine which French business legal forms an entrepreneur is eligible for and get a recommendation using Vestafolio's simulator API after collecting the simulator inputs and user consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

Entrepreneurs, advisors, and agents supporting French business formation use this skill to collect profile details, call Vestafolio's simulator, and explain eligible legal forms and qualitative recommendations. It is suited to French legal-structure orientation, not tax or contribution calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends approved business profile fields to Vestafolio's external API for simulation.

Mitigation: Explain the destination and exact fields first, obtain user consent, and avoid sending optional household data, personal identifiers, credentials, files, or conversation history.

Risk: Users may treat qualitative business-structure orientation as definitive legal, tax, or contribution advice.

Mitigation: State that the output is an estimate for orientation, ground the answer in the simulator response, and direct users to appropriate follow-up tools or professional advice for quantitative or legal decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-choisir-regime)
- [Vestafolio choisir-regime API](https://www.vestafolio.com/api/tools/v1/choisir-regime)
- [Vestafolio interactive simulator](https://www.vestafolio.com/simulateurs/choisir-regime)
- [Vestafolio publisher profile](https://clawhub.ai/user/vestafolio)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown, Shell commands]

**Output Format:** [Markdown with summarized simulator results and optional inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should be grounded in the Vestafolio API result and may be in French when the user writes in French.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
