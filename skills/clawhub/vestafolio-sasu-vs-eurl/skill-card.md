## Description:

Compares SASU and EURL net director income for a French solo entrepreneur by gathering the required inputs and calling Vestafolio's simulator API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and advisors use this skill to compare SASU and EURL outcomes for a French solo business, including salary, dividends, tax, social contributions, alerts, and the simulator recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires sharing business and tax inputs with Vestafolio's simulator API.

Mitigation: Confirm the user is comfortable sending those inputs before calling the API.

Risk: Simulator output is an estimate and may be mistaken for tax or legal advice.

Mitigation: State that results are estimates, explain assumptions and limits, and recommend professional review for decisions.

Risk: Network or API failure could prevent a grounded calculation.

Mitigation: If execution is unavailable or the API fails, say the calculation could not be completed and provide the interactive simulator link.

## Reference(s):

- [Vestafolio SASU vs EURL Skill](https://clawhub.ai/vestafolio/skills/vestafolio-sasu-vs-eurl)
- [Vestafolio SASU vs EURL Simulator](https://www.vestafolio.com/simulateurs/sasu-vs-eurl)
- [Vestafolio SASU vs EURL API Schema](https://www.vestafolio.com/api/tools/v1/sasu-vs-eurl)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Guidance]

**Output Format:** [Markdown response grounded in simulator API results, with optional inline shell commands when execution is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are estimates and should not be treated as tax or legal advice.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
