## Description:

ArchLang helps agents create, edit, and inspect architectural floor plans as code, then compile them into professional drawing formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use ArchLang to create, modify, and inspect building layouts as text, validate a plan against design constraints, and export the resulting drawing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package command is unpinned and may resolve to a changed release.

Mitigation: Review the package version and its changes before installation or execution.

Risk: A shared playground link may expose floor-plan details to people with access to the link.

Mitigation: Check the link contents and access scope before sharing plans, especially sensitive layouts.

Risk: The security scan had partial coverage because referenced paths were missing.

Mitigation: Treat the scan result as limited assurance and review the release files before use.

## Reference(s):

- [ArchLang release on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)
- [ArchLang plan schema](https://archlang.uk/plan.schema.json)
- [ArchLang intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files, Guidance]

**Output Format:** [ArchLang source text, command-line instructions, and compiled floor-plan files such as SVG, PNG, PDF, DXF, TXT, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated drawings and plan data depend on the user's brief and selected export format.]

## Skill Version(s):

1.59.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
