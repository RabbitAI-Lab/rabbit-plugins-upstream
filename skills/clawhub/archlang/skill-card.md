## Description:

Use ArchLang to create, edit, or inspect architectural floor plans as code and compile `.arch` files into professional SVG, PNG, PDF, or DXF drawings through the `archlang` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chanmeng666](https://clawhub.ai/user/chanmeng666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architectural design agents use ArchLang to draft, revise, inspect, and validate building floor plans from text-based plans, then export drawings and quantity takeoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The zero-install setup uses an unpinned npm package version, and the security scan was partial because some local references could not be resolved.

Mitigation: Pin and review the package version before installation, and inspect unresolved references before use.

## Reference(s):

- [ArchLang plan schema](https://archlang.uk/plan.schema.json)
- [ArchLang intent schema](https://archlang.uk/intent.schema.json)
- [ArchLang grammar (GBNF)](https://archlang.uk/archlang.gbnf)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Files, Guidance]

**Output Format:** [ArchLang source text, CLI commands, and generated SVG, DXF, TXT, PDF, PNG, Plan JSON, CSV, or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated drawing and data formats depend on the requested export.]

## Skill Version(s):

1.65.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
