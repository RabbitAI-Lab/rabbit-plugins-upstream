## Description:

Compute French notary fees (frais de notaire) for a property purchase by department and property type using Vestafolio's simulator API after collecting the required purchase inputs and user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and real-estate professionals use this skill to estimate French property purchase closing costs, including DMTO, notary emoluments, disbursements, CSI, and optional mortgage registration fees. It is intended for scenario-specific estimates after the user provides purchase details and approves sending the limited inputs to Vestafolio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill can send purchase price, property type, department, first-time-buyer status, mortgage inclusion, and loan amount to Vestafolio's external API.

Mitigation: Inform the user of the destination and exact fields before calling the API, obtain approval for that scope, and omit names, addresses, credentials, documents, account identifiers, and conversation history.

Risk: The API result is an estimate and may not match the final amount fixed by the notary at signing.

Mitigation: Ground answers in the API result, state assumptions and limits, and avoid presenting the estimate as legal or tax advice.

## Reference(s):

- [Vestafolio frais de notaire API schema](https://www.vestafolio.com/api/tools/v1/frais-notaire)
- [Vestafolio frais de notaire simulator](https://www.vestafolio.com/simulateurs/frais-notaire)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown]

**Output Format:** [Markdown response with calculation summary and optional inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fee breakdowns, assumptions, limits, and a simulator link when useful.]

## Skill Version(s):

1.0.2 (source: server release metadata); artifact frontmatter reports 1.2.1

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
