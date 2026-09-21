## Description:

Retrieves and answers questions from a local knowledge-base directory using layered data_structure.md indexes, progressive bounded search across Markdown, text, PDF, and Excel files, and source-aware responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, developers, and agents use this skill to retrieve information from local knowledge-base directories and produce grounded answers with file references. It is also used, with explicit confirmation, to generate directory indexes or derived PDF text files for local retrieval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to read a local knowledge-base directory that may contain sensitive documents.

Mitigation: Install and use it only for intended local directories, confirm the knowledge-base root before retrieval, and review file references in generated answers.

Risk: Optional maintenance actions can create index files, PDF-derived text files, or OCR page images.

Mitigation: Run those actions only after explicit user confirmation of the target path and expected outputs.

Risk: Optional PDF, Excel, or OCR dependencies modify the active Python environment.

Mitigation: Approve dependency installation only when those document types need processing and use the pinned optional requirements supplied with the artifact.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-kb-retriever)
- [GitHub Repository](https://github.com/dtsola/xiaoyaoclaw-kb-retriever)
- [Yuque OpenClaw Guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [PDF Reading Guide](references/pdf_reading.md)
- [Excel Reading Guide](references/excel_reading.md)
- [Excel Analysis Guide](references/excel_analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with file references, command snippets, and optional generated local helper files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Core retrieval is read-only and local; optional maintenance writes require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
