## Description:

Use when the user wants to create, edit, or inspect an architectural floor plan / building layout as code — e.g. "draw a 2-bedroom apartment", "add a bathroom to this plan", "make the bedroom 1 m wider", "lay out an office floor". ArchLang is a tiny text language that compiles a .arch file to a professional floor-plan drawing (SVG/PNG/PDF/DXF). Drive it entirely through the `archlang` CLI; do not hand-render.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Architects, designers, and developers can use ArchLang through an agent to draft, edit, and inspect building layouts as text, then produce floor-plan drawings and structured reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package commands without pinned versions may run an unreviewed release.

Mitigation: Pin reviewed package versions and inspect release details before running package commands.

Risk: Sharing a plan-bearing playground link may expose floor-plan information.

Mitigation: Review the plan and link visibility before sharing, and remove sensitive details when needed.

## Reference(s):

- [ArchLang Intent Schema](https://archlang.uk/intent.schema.json)
- [ArchLang Plan Schema](https://archlang.uk/plan.schema.json)
- [ArchLang GBNF](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Files, Text, JSON, CSV, Markdown]

**Output Format:** [ArchLang source and compiled SVG, PNG, PDF, DXF, TXT, Plan JSON, CSV, or Markdown outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available formats depend on the selected ArchLang CLI command.]

## Skill Version(s):

1.61.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
