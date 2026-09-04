## Description:

house-skills-kit provides a Chinese real-estate AI skill kit with local calculators, sales SOPs, talk tracks, lead-grading workflows, mortgage guidance, opening-day execution guidance, and templates for generating branded advisor skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

Real-estate professionals, developers, and agent operators use this kit to select, install, or generate Chinese property-domain skills for sales teams and advisory workflows. Calculation outputs and customer-facing guidance require local policy and compliance review before operational use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can overwrite files in an existing agent skills folder.

Mitigation: Review the rendered skill directory and installation destination before running install.sh.

Risk: Calculator policy data is demo/reference material and may not reflect current local rules.

Mitigation: Check current official local rules before using outputs for business, customer, tax, loan, or compliance decisions.

Risk: Templates and workflows may be adapted to customer or channel records in real deployments.

Mitigation: Add appropriate access controls, consent handling, and data-retention rules before processing real customer or channel data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/danfeistar/skills/house-skills-kit)
- [Source overview](README.md)
- [Skill definition](SKILL.md)
- [Calculator toolkit documentation](skills/calc-toolkit/README.md)
- [Sales talk library documentation](skills/sales-talk-library/README.md)
- [Sales objection handling documentation](skills/sales-objection-handling/README.md)
- [Sales lead grading documentation](skills/sales-lead-grading/README.md)
- [Sales mortgage SOP documentation](skills/sales-mortgage-sop/README.md)
- [Sales opening SOP documentation](skills/sales-opening-sop/README.md)
- [Kunming example](examples/kunming/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional shell commands, YAML configuration, and Python command-line code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calculator results and generated skill skeletons should be reviewed against current local real-estate rules before operational use.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
