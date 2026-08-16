## Description:

Converts building codes, GB standards, industry rules, and regulations from PDFs into structured, queryable AI skills with indexed clauses, preserved mandatory wording, extracted tables, and cross-reference maps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[51comic](https://clawhub.ai/user/51comic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and engineering teams use this skill to turn regulation PDFs into searchable agent skills for clause lookup, table extraction, and cross-standard reference review. It is especially oriented toward Chinese building-design codes and GB standards, while allowing other technical regulations when the user supplies the source PDF.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow executes local helper tools for PDF extraction and scanning.

Mitigation: Approve execution only after confirming the book-to-skill tool path comes from a trusted local installation.

Risk: Generated regulation skills may contain extraction errors or legal-force wording mistakes.

Mitigation: Review generated files against the source regulation PDF and verify legal wording accuracy before relying on the output for professional work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/51comic/skills/code-to-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command blocks and generated skill files, including clause Markdown, table JSON, indexes, maps, and configuration metadata.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local regulation PDF and a trusted book-to-skill installation path before extraction commands are approved.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
