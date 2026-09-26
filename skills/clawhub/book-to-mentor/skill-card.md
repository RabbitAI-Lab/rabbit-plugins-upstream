## Description:

Convert a book or document into a dedicated mentor skill with source-grounded explanations, guided practice, and learning records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gengwenhao](https://clawhub.ai/user/gengwenhao)

### License/Terms of Use:

MIT

## Use Case:

Developers, writers, educators, and learners use this skill to turn user-provided books or documents into reusable mentor skills with source-grounded explanations, guided practice, quick-reference material, and learning records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided book files or folders and writes extracted text, summaries, mentor files, and learning records.

Mitigation: Use a dedicated work and output folder, avoid broad home-directory globs, and review generated mentor and state files before sharing or installing them.

Risk: Optional parser dependencies may be needed for some formats, and extraction success does not prove complete layout or semantic fidelity.

Mitigation: Install only the parsers needed for the source format, inspect extraction metadata and representative excerpts, and disclose partial or failed coverage in the generated mentor.

Risk: Source documents can contain embedded instructions that should not become agent rules or tool permissions.

Mitigation: Treat source material as reference data, check for source-instruction leakage during validation, and keep generated teaching behavior grounded in verified source content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gengwenhao/skills/book-to-mentor)
- [Sources and extraction](docs/formats.md)
- [Learning record contract v1](docs/state-schema.en.md)
- [GitHub Issues](https://github.com/gengwenhao/book-to-mentor/issues)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files, JSON learning records, Python helper scripts, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a mentor directory from user-selected source documents; extraction coverage and learning records should be reviewed before use.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
