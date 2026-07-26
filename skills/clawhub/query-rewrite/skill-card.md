## Description: <br>
RAG retrieval pre-processing layer that detects whether a query needs rewriting, applies one of six rewrite modes when needed, then searches with both original and rewritten queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dabin0927](https://clawhub.ai/user/dabin0927) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill before RAG retrieval, memory search, wiki search, or vector search to resolve ambiguous, contextual, comparative, multi-intent, rhetorical, or condition-heavy queries while retaining the original query. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Retrieval searches may be expanded with recent conversation context, which could expose context to memory, wiki, or vector search systems where that context should not be sent. <br>
Mitigation: Use the skill only in RAG workflows where sending recent conversation context to retrieval systems is acceptable, and disable it for conversations with restricted context-sharing requirements. <br>
Risk: Ambiguous queries can be rewritten too broadly or with the wrong referent, reducing retrieval precision or changing the intended search focus. <br>
Mitigation: Keep the original query in every search path, apply the documented intent-fidelity and zero-rewrite rules, and fall back to the original query when context or intent is unclear. <br>


## Reference(s): <br>
- [Rewrite patterns reference](references/rewrite-patterns.md) <br>
- [Project homepage](https://github.com/DaBin0927/query-rewrite#readme) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance and rewritten query strings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce one or more rewritten queries, preserves the original query for retrieval, and falls back to the original query when context or intent is unclear.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
