## Description:

Compute gross and net rental yield and monthly cash-flow for a French buy-to-let investment from acquisition cost, rent and annual charges using Vestafolio's simulator API, after asking the simulator's questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to estimate gross yield, net yield, and pre-financing monthly cash flow for French rental property scenarios. It is intended for rental profitability questions where the user can provide acquisition costs, rent, annual charges, management fees, and vacancy assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send rental profitability inputs to Vestafolio's external API.

Mitigation: Explain the destination and data scope, summarize the fields to be sent, obtain user approval, and omit unrelated personal data before posting.

Risk: The profitability result may be misunderstood as complete investment advice.

Mitigation: State assumptions and limits, ground answers in the API result, and note that financing and rental-income taxation are outside this calculation.

## Reference(s):

- [Vestafolio rental profitability simulator](https://www.vestafolio.com/simulateurs/rentabilite-locative)
- [Vestafolio rental profitability API schema](https://www.vestafolio.com/api/tools/v1/rentabilite-locative)
- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-rentabilite-locative)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with calculated results, assumptions, caveats, and optional inline API or curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Replies in French when the user writes in French; results must be grounded in the simulator API response.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
