## Description:

Compare French micro-entreprise vs regime reel and versement liberatoire with actual Vestafolio API calls for consulting or freelance regime choices, projected revenue and expenses, cotisations, ACRE, and VL eligibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial/tax assistants use this skill to collect the required French micro-entreprise simulator inputs, obtain consent for Vestafolio API use, execute the calculation, and explain the resulting micro, versement liberatoire, and regime reel comparison. It is suited to first-pass quantitative regime decisions and eligibility checks, not standalone tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed to send user-provided financial and tax simulator inputs to Vestafolio's external API.

Mitigation: Before any API call, summarize the fields and values to be transmitted, explain the Vestafolio destination, and proceed only after explicit user agreement.

Risk: Users may treat simulator estimates or current coded tax rates as definitive tax advice.

Mitigation: Ground results in the API response, state relevant assumptions and limits, describe estimates as not tax advice, and provide the simulator link for manual review when useful.

Risk: API unavailability, HTTP failure, or missing execution tools can prevent a completed calculation.

Mitigation: Report that the calculation could not be completed, avoid inventing results or recommendations, and offer the manual simulator link instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-micro-entreprise)
- [Vestafolio micro-entreprise API endpoint](https://www.vestafolio.com/api/tools/v1/micro-entreprise)
- [Vestafolio micro-entreprise simulator](https://www.vestafolio.com/simulateurs/micro-entreprise)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Code, Guidance]

**Output Format:** [Markdown narrative with API request details and calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user approval before transmitting simulator inputs to Vestafolio; final answers should disclose assumptions, API failures, and simulator limitations.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
