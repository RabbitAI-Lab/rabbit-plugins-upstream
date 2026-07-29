## Description: <br>
Builds and searches lightweight TurboVec document indexes for low-memory semantic search and RAG workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rochyroch](https://clawhub.ai/user/rochyroch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build compact semantic-search indexes from Markdown or text documents and query them with vector, hybrid BM25, reranked, or JSON-output search modes. It is aimed at personal, team, embedded, and resource-constrained RAG workflows rather than high-stakes recall-critical applications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes local-private Supabase and WhatsApp workflow instructions that do not match the public document-search scope. <br>
Mitigation: Treat those local instructions as private evidence, not user guidance; for normal use, follow only the public TurboVec indexing and search workflow unless you intentionally control that backend. <br>
Risk: Document text and queries are sent to the configured embedding API, and a non-local endpoint can expose sensitive content. <br>
Mitigation: Use a local or fully trusted embedding endpoint for sensitive documents, and verify any --api host before building or searching an index. <br>
Risk: Generated index directories include chunks.json with full document text. <br>
Mitigation: Restrict access to index directories and avoid sharing them unless the underlying documents are safe to disclose. <br>
Risk: Quantized vector search can have ranking variance and may miss or reorder important results. <br>
Mitigation: Avoid using this skill as the sole retrieval mechanism for medical, legal, financial, or other recall-critical workflows; validate recall with representative queries. <br>
Risk: Legacy BM25 pickle indexes can present arbitrary code execution risk if loaded by older tooling. <br>
Mitigation: Use the current JSON BM25 index format and rebuild legacy indexes; the included search script refuses legacy pickle files. <br>


## Reference(s): <br>
- [TurboVec Quantization Explained](references/quantization.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/rochyroch/skills/the-librarian) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; scripts produce index files and optional JSON search results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Build output can include library.qindex, chunks.json, bm25_index.json, and stats.json. Search output can be human-readable text or JSON.] <br>

## Skill Version(s): <br>
1.2.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
