## Description:

house-skills-kit helps agents generate and use Chinese real-estate skills, including a calculator toolkit for mortgage, transaction-cost, eligibility, yield, commission, and policy-sensitive property calculations plus templates for brand-specific advisor skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

Real-estate developers, brokerages, agents, advisors, and buyers use this skill to select or install property workflows, run local Python calculators, and generate brand-specific Chinese real-estate advisor skills.

### Deployment Geography for Use:

Global, with built-in examples and rule data focused on China.

## Known Risks and Mitigations:

Risk: Generated skills may trigger too broadly if their activation keywords are not narrowed to the intended city, project, role, and user intent.

Mitigation: Review and narrow generated trigger keywords before installing or publishing a generated skill.

Risk: CRM, attribution, or referral workflows may record customer or referral information without adequate notice.

Mitigation: Tell users what personal data will be recorded, where it will be stored, and how official registration or reward processing works before enabling those modules.

Risk: Real-estate policy, tax, fee, and financing calculations can become stale or differ by locality.

Mitigation: Validate rule data against current official city notices and local operating policy before using outputs for formal business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/danfeistar/skills/house-skills-kit)
- [Repository overview](README.md)
- [Calculator toolkit skill](skills/calc-toolkit/SKILL.md)
- [Calculator toolkit README](skills/calc-toolkit/README.md)
- [Kunming district reference](examples/kunming/references/plates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples, configuration files, and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local calculators use repository rule data and can be overridden with user-provided templates or command-line parameters.]

## Skill Version(s):

1.4.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
