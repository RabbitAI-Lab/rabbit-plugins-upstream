## Description:

Knowledge Engineering helps agents turn long RAG knowledge-base documents into semantically complete, retrieval-ready Markdown slices with validation, auditing, and retrieval evaluation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ebandao777-oss](https://clawhub.ai/user/ebandao777-oss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-base maintainers use this skill to convert long technical documents into atomic Markdown slices for RAG systems. The workflow supports slice planning, generated Markdown outputs, validation, cross-reference auditing, and retrieval-quality evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write, repair, or overwrite many Markdown slice files in a selected output directory.

Mitigation: Run it in a project-specific or disposable workspace, review the planned output directory first, keep backups of valuable slices, and avoid --fix or --renumber on important directories without review.

Risk: Retrieval evaluation may install sentence-transformers or download a local embedding model.

Mitigation: Use a project-specific Python environment and review dependency installation or model download behavior before running retrieval evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ebandao777-oss/skills/knowledge-engineering)
- [Server-resolved source repository](https://github.com/ebandao777-oss/knowledge-engineering)
- [README](artifact/README.md)
- [Quickstart](artifact/QUICKSTART.md)
- [Reference manual](artifact/REFERENCE.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown slice files with YAML frontmatter, JSON plans or reports, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces source-specific output directories, validation and audit reports, retrieval evaluation reports, and optional structured exports for large tables.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact SKILL.md frontmatter reports 5.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
