## Description:

Compare French micro-entreprise, régime réel, and versement libératoire scenarios using Vestafolio API calls after collecting the simulator inputs needed for a grounded recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vestafolio](https://clawhub.ai/user/vestafolio)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting French freelancers use this skill to compare micro-entreprise, régime réel, and versement libératoire outcomes from projected revenue, expenses, ACRE status, household tax inputs, and eligibility details. It is suited to estimate-oriented regime choice support, not formal tax advice.

### Deployment Geography for Use:

France

## Known Risks and Mitigations:

Risk: Financial and tax details provided for a simulation are sent to Vestafolio's API.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid sending unnecessary personal or sensitive details.

Risk: Simulator outputs are estimates rather than tax advice.

Mitigation: Treat results as decision support and verify consequential choices with current official sources or a qualified tax professional.

## Reference(s):

- [Vestafolio micro-entreprise API](https://www.vestafolio.com/api/tools/v1/micro-entreprise)
- [Vestafolio interactive micro-entreprise simulator](https://www.vestafolio.com/simulateurs/micro-entreprise)
- [ClawHub skill page](https://clawhub.ai/vestafolio/skills/vestafolio-micro-entreprise)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, API Calls, Shell commands, Code]

**Output Format:** [Markdown or text response summarizing simulator JSON results and relevant assumptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a successful Vestafolio API call for numerical results; outputs are estimates and not tax advice.]

## Skill Version(s):

1.2.1 (source: artifact/SKILL.md frontmatter and release changelog text; ClawHub release metadata version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
