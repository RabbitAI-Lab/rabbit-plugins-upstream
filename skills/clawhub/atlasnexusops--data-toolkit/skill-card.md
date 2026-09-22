## Description:

Complete data conversion, validation, and cleaning toolkit for converting between JSON, CSV, YAML, and XML, validating schemas, and cleaning duplicates and nulls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[atlasnexusops](https://clawhub.ai/user/atlasnexusops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data engineers use this skill to convert local datasets between common structured formats, validate JSON or CSV data, and clean duplicates, nulls, and normalized values in data-processing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The data-cleaning workflow can overwrite source datasets when no output path is provided.

Mitigation: Use explicit --output paths, run on copies or backups, and review changed files before relying on processed data.

Risk: Local processing scripts depend on runtime tools and Python packages that may vary by environment.

Mitigation: Install dependencies in a pinned virtual environment and verify node, python3, PyYAML, and optional pandas availability before use.

## Reference(s):

- [ClawHub Data Toolkit skill page](https://clawhub.ai/atlasnexusops/skills/data-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local data-processing guidance and commands that may create or rewrite JSON, CSV, YAML, and XML files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
