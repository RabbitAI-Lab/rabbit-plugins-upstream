## Description:

Project compound-interest growth of an investment with initial capital and monthly contributions using Vestafolio's simulator API, after asking the simulator's questions (initial capital, monthly contribution, duration, annual return, compounding frequency).

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to calculate compound-interest projections with initial capital, recurring contributions, duration, annual return, and compounding frequency. It returns estimates and year-by-year invested-versus-gains tables through Vestafolio's simulator after explicit approval for the API call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Investment inputs may be sent to Vestafolio's external API.

Mitigation: Summarize the destination and fields before transmission, obtain explicit user approval, and omit credentials, account identifiers, personal identifiers, files, and unrelated conversation history.

Risk: Compound-interest projections can be mistaken for guaranteed returns or investment advice.

Mitigation: Ground results in the API response, state assumptions and limits, and clarify that estimates are pre-tax and exclude fees.

## Reference(s):

- [Vestafolio Compound Interest API](https://www.vestafolio.com/api/tools/v1/interets-composes)
- [Vestafolio Compound Interest Simulator](https://www.vestafolio.com/simulateurs/interets-composes)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown response with numeric summaries and a year-by-year table when the API call succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should state assumptions and limits, and should not include tax treatment, fees, or investment advice.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter and release changelog report 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
