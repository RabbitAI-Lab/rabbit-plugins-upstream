## Description:

A role-based collection of Chinese real-estate AI skills for buyers, brokers, developers, sales teams, and marketers, including calculation tools, workflow guidance, and reusable templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[danfeistar](https://clawhub.ai/user/danfeistar)

### License/Terms of Use:

Apache-2.0

## Use Case:

Chinese real-estate buyers, brokers, developers, sales teams, and marketers use the skills to get role-specific transaction guidance, sales and marketing workflows, and property calculations, or to generate branded advisory skills from templates.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious and reports unsafe file-writing paths; the available evidence does not establish malicious intent.

Mitigation: Review the renderer's file-path handling before installation.

Risk: The security summary reports possible inconsistencies in financial calculations.

Mitigation: Cross-check calculations and policy values with current local official sources before relying on them.

Risk: Customer-facing workflows may involve identifiable customer information.

Mitigation: Do not send identifiable customer information to an AI service unless your organization has approved the processing and suitable privacy controls are in place.

Risk: The security scan was partial: 139 of 140 components were scanned, and one file had limited static analysis.

Mitigation: Review the incompletely analyzed component before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/danfeistar/skills/house-skills-kit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance, calculation results, Python code, shell commands, and YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some calculations use city-specific policy rules that should be checked against current official sources.]

## Skill Version(s):

1.8.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
