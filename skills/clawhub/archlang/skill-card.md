## Description:

ArchLang is a tiny text language that compiles .arch files into floor-plan drawings in SVG, PNG, PDF, DXF, TXT, or Plan JSON formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use ArchLang to create, edit, validate, and inspect building floor plans as code, then export drawings and room or quantity summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI setup can install and run changing, unpinned npm package versions.

Mitigation: Pin and review package versions before running the CLI.

Risk: Hosted playground links may expose floor-plan content through an upload, the link, or its visibility settings.

Mitigation: Check whether the plan is uploaded, embedded in the link, or visible to others before sharing.

Risk: The security scan was partial because it could not resolve several referenced files, so it does not establish that the skill is safe.

Mitigation: Review the complete package and unresolved referenced files before use.

## Reference(s):

- [ArchLang on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)
- [Plan JSON schema](https://archlang.uk/plan.schema.json)
- [Intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar (GBNF)](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Files, Text, Shell commands]

**Output Format:** [ArchLang source and floor-plan exports (SVG, PNG, PDF, DXF, TXT, or Plan JSON), with room and quantity summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plans use millimetres; CLI commands can validate and describe them.]

## Skill Version(s):

1.62.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
