## Description:

Analyzes and optimizes retrieval-augmented generation pipelines for 100K-2M token documents using hybrid search, chunking, multi-document reasoning, evaluation, and structured reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gechengling](https://clawhub.ai/user/gechengling)

### License/Terms of Use:

MIT-0

## Use Case:

Financial analysts, legal professionals, researchers, and developers use this skill to design, evaluate, and improve long-context RAG workflows for large document collections. It helps choose chunking strategies, configure hybrid retrieval, measure retrieval quality, reason across documents, and produce structured reports with source-aware checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive or unauthorized documents could be included in long-context analysis.

Mitigation: Use only documents the user is authorized to process, limit intake to the minimum needed set, and redact sensitive personal or business data where possible.

Risk: Generated reports or exports could expose sensitive content if saved or shared without review.

Mitigation: Show the complete report or export preview and require explicit user confirmation before saving, exporting, or sending it.

Risk: RAG outputs for financial or legal material can be misleading when conclusions lack source support.

Mitigation: Require citations or source locations for material conclusions and have qualified reviewers check outputs before decision-making use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gechengling/skills/long-context-rag-analyzer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with structured reports, tables, checklists, and illustrative code or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The artifact requires preview and explicit user confirmation before any report, export, or file write is saved or shared.]

## Skill Version(s):

3.0.3 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
