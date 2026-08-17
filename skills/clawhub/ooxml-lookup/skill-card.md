## Description:

Query the ECMA-376 Office Open XML schema offline to determine legal OOXML elements, child order, attributes, values, namespaces, profiles, and validation-error context for .docx, .xlsx, and .pptx markup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shbernal](https://clawhub.ai/user/shbernal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when writing, reading, or debugging Office Open XML markup and need local answers about schema legality, valid children, attributes, values, namespaces, profile differences, or validator diagnostic context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advanced SQL queries can be expensive even though the bundled database is opened read-only.

Mitigation: Prefer the documented subcommands, use limits for broad searches or SQL, and avoid unbounded joins during routine agent workflows.

Risk: Schema lookup results can be misleading if treated as document validation, Office application behavior, specification prose, or semantic search.

Mitigation: Use this skill for schema-permitted structures only, validate files with a separate validator, and consult specification or implementation references for behavior questions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shbernal/skills/ooxml-lookup)
- [Release changelog](https://github.com/shbernal/ooxml-ai-tooling/releases/tag/v0.0.4)
- [OOXML reference site](https://ooxml.dev)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [JSON command output with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands run locally against a bundled read-only SQLite OOXML schema database; stdout is JSON.]

## Skill Version(s):

0.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
