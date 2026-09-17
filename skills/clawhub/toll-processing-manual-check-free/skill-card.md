## Description:

Checks toll-processing manual and bonded-material reconciliation tables by recalculating line formulas, totals, duplicate rows, blanks, and negative values, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Customs, documentation, finance, and compliance staff use this Chinese-language skill to check toll-processing manual reconciliation tables before monthly customs close or manual cancellation. It recalculates declared consumption, balances, totals, duplicate rows, blanks, and negative values when the input includes the required table headers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker appears local, but the documentation and normal output steer users toward agent-run paid installation and purchase instructions.

Mitigation: Do not let an agent run SkillPay installation commands, install additional skills, or initiate payment unless the user independently verifies the source and explicitly chooses to proceed.

Risk: The free release omits several checks that are listed as paid-version functionality.

Mitigation: Treat results as limited to the executed free checks and review the listed non-run and out-of-scope checks before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/toll-processing-manual-check-free)
- [Source skill instructions](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Console text or JSON findings with row-level source references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; insufficient input returns missing fields instead of a substantive finding.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
