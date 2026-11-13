## Description:

Use when the user wants to create, edit, or inspect an architectural floor plan / building layout as code — e.g. "draw a 2-bedroom apartment", "add a bathroom to this plan", "make the bedroom 1 m wider", "lay out an office floor". ArchLang is a tiny text language that compiles a .arch file to a professional floor-plan drawing (SVG/PNG/PDF/DXF). Drive it entirely through the `archlang` CLI; do not hand-render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design teams use ArchLang to create, edit, inspect, and validate architectural floor plans through a command-line workflow. It produces plan source and drawings or structured plan data for review and further use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package commands are unpinned, and playground links may contain floor-plan information; scanner coverage is partial.

Mitigation: Review package commands before running them, avoid sharing links for sensitive layouts, and check unresolved references before relying on the scan.

## Reference(s):

- [ArchLang on ClawHub](https://clawhub.ai/chanmeng666/skills/archlang)
- [ArchLang intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang Plan schema](https://archlang.uk/plan.schema.json)
- [ArchLang GBNF](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Analysis, Files]

**Output Format:** [ArchLang (.arch) source, shell commands, and floor-plan outputs in SVG, PNG, PDF, DXF, TXT, CSV, Markdown, or Plan JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Floor-plan geometry and validation results follow the user's brief and the supplied plan.]

## Skill Version(s):

1.60.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
