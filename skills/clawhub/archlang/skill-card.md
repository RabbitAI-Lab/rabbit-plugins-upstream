## Description:

Creates, edits, and inspects code-based architectural floor plans with the ArchLang CLI, compiling `.arch` plans into drawings and structured outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and design teams can author or edit building layouts as `.arch` source, then validate room geometry and relationships and export floor-plan drawings or structured plan data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented zero-install setup runs an npm package without pinning a version, creating supply-chain exposure if that package changes.

Mitigation: Review the package and installer sources, and install an exact, reviewed version.

Risk: Shared playground links may expose floor-plan content depending on their sharing behavior.

Mitigation: Check sharing behavior before sending a playground link containing a plan.

## Reference(s):

- [ArchLang on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)
- [Plan JSON schema](https://archlang.uk/plan.schema.json)
- [Intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files]

**Output Format:** [ArchLang `.arch` source and floor-plan outputs in SVG, PNG, PDF, DXF, TXT, or Plan JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic compilation with validation diagnostics and optional automated fixes.]

## Skill Version(s):

1.66.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
