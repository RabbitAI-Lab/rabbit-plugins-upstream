## Description:

Compare final net wealth between buying a primary residence with a mortgage and renting while investing savings, over a chosen horizon, using Vestafolio's simulator API, after asking the simulator's questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and assistants use this skill to compare buying a primary residence in France against renting and investing available savings. It collects the simulator inputs, requests approval before sending them to Vestafolio, and explains the API result as an estimate rather than financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved calculator inputs are sent to Vestafolio's external API.

Mitigation: The skill summarizes fields and values before submission, requires user agreement, and instructs the agent to omit unnecessary identifying details.

Risk: The buy-versus-rent result can be sensitive to market, rent, tax, and investment-return assumptions.

Mitigation: The skill tells the agent to present assumptions and limits, treat outputs as estimates, and avoid presenting the result as financial advice.

Risk: Network failure, API failure, or validation errors can prevent a completed simulation.

Mitigation: The skill instructs the agent to report that the calculation could not be completed, explain rejected fields when available, and avoid inventing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-achat-vs-location)
- [Vestafolio simulator API schema](https://www.vestafolio.com/api/tools/v1/achat-vs-location)
- [Vestafolio achat-vs-location simulator](https://www.vestafolio.com/simulateurs/achat-vs-location)
- [Vestafolio](https://www.vestafolio.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown or conversational prose with calculator result fields, assumptions, limits, and next questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include French-language responses, approved API request summaries, scenario comparisons, sensitivity caveats, and simulator links.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
