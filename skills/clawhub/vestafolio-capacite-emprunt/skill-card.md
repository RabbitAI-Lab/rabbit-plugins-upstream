## Description:

Estimates the maximum mortgage a French household can borrow from income, existing charges, loan rate, loan duration, insurance rate, and the HCSF 35% debt-ratio rule using Vestafolio's simulator API after user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to estimate French mortgage borrowing capacity and property-budget scenarios from household income, fixed charges, rate, duration, insurance rate, and the HCSF debt-ratio rule. The skill asks for missing inputs, obtains approval before transmitting them, and grounds answers in Vestafolio's simulator API output.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: The skill transmits approved mortgage inputs to Vestafolio's external API.

Mitigation: Summarize the destination and exact fields before each uncovered POST, obtain explicit user approval, and send only required simulator fields.

Risk: Users may treat the output as a bank approval or financial advice.

Mitigation: State that results are estimates, not bank pre-approval or financial advice, and ground numeric answers in the API result.

Risk: Extra personal or financial details could be shared unnecessarily.

Mitigation: Do not transmit names, addresses, account identifiers, credentials, files, conversation history, or unrelated financial details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-capacite-emprunt)
- [Vestafolio simulator](https://www.vestafolio.com/simulateurs/capacite-emprunt)
- [Vestafolio API schema and endpoint](https://www.vestafolio.com/api/tools/v1/capacite-emprunt)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, API Calls, shell commands]

**Output Format:** [Markdown with concise natural-language guidance, calculation summaries, API-result interpretation, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies in French when the user writes in French; sends only approved simulator fields to the external API.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
