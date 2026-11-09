## Description:

Use when the user wants to create, edit, or inspect an architectural floor plan or building layout as code; ArchLang compiles a .arch file to a floor-plan drawing through the archlang CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design teams use this skill to create, revise, inspect, and export architectural floor plans from text-based plans. It supports checking room relationships, dimensions, and common layout issues during that workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded CLI tools, the optional renderer, related skills, and linked schemas are outside the bundled skill and have not been audited.

Mitigation: Prefer a reviewed, version-pinned CLI installation and review the external components before use.

Risk: Edits to a floor plan can introduce unintended changes.

Mitigation: Preview plan changes and keep backups before applying edits.

Risk: Shareable playground links may expose plan details.

Mitigation: Review plan contents and sharing settings before creating or distributing a playground link.

## Reference(s):

- [ArchLang plan schema](https://archlang.uk/plan.schema.json)
- [ArchLang intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar (GBNF)](https://archlang.uk/archlang.gbnf)
- [ArchLang on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)

## Skill Output:

**Output Type(s):** [Code, Files, Text, Markdown, Shell commands]

**Output Format:** [ArchLang .arch source, floor-plan exports (SVG, PNG, PDF, DXF, TXT, or Plan JSON), and CLI reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output format depends on the requested plan and export.]

## Skill Version(s):

1.57.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
