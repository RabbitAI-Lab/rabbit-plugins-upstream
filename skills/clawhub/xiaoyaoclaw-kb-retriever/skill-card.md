## Description:

OpenClaw Knowledge Base Retriever helps agents answer questions from local Markdown, PDF, and Excel knowledge-base directories using hierarchical data_structure.md indexes, progressive retrieval, and optional on-demand Python processing for PDF and Excel files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve and answer questions from a local knowledge-base directory while keeping source files unchanged. It is intended for local indexed navigation, targeted text search, and structured PDF or Excel processing when a question requires those file types.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads a user-selected local knowledge-base directory, which may contain sensitive or private content.

Mitigation: Use it only on intended directories and review retrieved excerpts before sharing outputs outside the local workflow.

Risk: Optional helper scripts can create local indexes, extracted PDF text, or page images, and --force index rebuilds can overwrite existing data_structure.md files.

Mitigation: Review prompts before approving file creation or --force rebuilds, and keep outputs in temporary or user-specified locations when possible.

Risk: Advanced PDF or Excel processing may require pip package installation that changes the local Python environment.

Mitigation: Install only the documented packages after explicit user confirmation, and avoid dependency installation when core text retrieval is sufficient.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-kb-retriever)
- [Publisher profile](https://clawhub.ai/user/dtsola)
- [Complete documentation link from skill text](https://github.com/dtsola/xiaoyaoclaw-kb-retriever)
- [Yuque overview link from skill text](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [PDF reading reference](references/pdf_reading.md)
- [Excel reading reference](references/excel_reading.md)
- [Excel analysis reference](references/excel_analysis.md)
- [data_structure.md template](templates/data_structure.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with source references and inline shell or Python command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local data_structure.md indexes, extracted PDF text, or page images when required by retrieval or explicitly requested by the user.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
