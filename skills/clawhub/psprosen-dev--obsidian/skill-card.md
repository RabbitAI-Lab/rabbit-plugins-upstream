## Description:

Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psprosen-dev](https://clawhub.ai/user/psprosen-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and Obsidian users use this skill to author valid Obsidian Bases files that organize vault notes into table, card, list, or map views with filters, formulas, summaries, and property display settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated Bases can expose note metadata or selected vault content in Obsidian views.

Mitigation: Review filters, displayed properties, formulas, and especially any HTML-rendering formulas before saving a .base file.

Risk: Invalid YAML or malformed formulas can prevent a Base from rendering correctly.

Mitigation: Validate YAML syntax, quote strings containing special characters, guard formulas against missing properties, and test the Base in Obsidian.

## Reference(s):

- [Obsidian Bases Syntax](https://help.obsidian.md/bases/syntax)
- [Obsidian Bases Functions](https://help.obsidian.md/bases/functions)
- [Obsidian Bases Views](https://help.obsidian.md/bases/views)
- [Obsidian Formulas](https://help.obsidian.md/formulas)
- [Complete Functions Reference](references/FUNCTIONS_REFERENCE.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with YAML examples for .base files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Obsidian Bases filters, formulas, view definitions, summaries, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
