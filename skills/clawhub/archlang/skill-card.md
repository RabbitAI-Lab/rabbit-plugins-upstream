## Description:

Use ArchLang to create, edit, or inspect architectural floor plans as code and compile .arch files to professional drawings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT

## Use Case:

Architects, designers, and developers can use the agent to draft, revise, inspect, validate, and export building floor plans from text briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions use unpinned npm commands, so the fetched package can change between runs.

Mitigation: Review the package instructions before installing; prefer an exact reviewed version with a lockfile-backed install, and limit CLI access to the files and environment it needs.

## Reference(s):

- [ArchLang on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)
- [ArchLang Plan JSON schema](https://archlang.uk/plan.schema.json)
- [ArchLang intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar (GBNF)](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files, Guidance]

**Output Format:** [ArchLang source (.arch), command-line instructions, and floor-plan files (SVG, PNG, PDF, DXF, TXT, or Plan JSON)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plan files can be validated and revised through the ArchLang CLI.]

## Skill Version(s):

1.67.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
