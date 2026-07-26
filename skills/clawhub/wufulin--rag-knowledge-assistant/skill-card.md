## Description: <br>
Builds and queries a local RAG knowledge base with BM25 and vector hybrid retrieval, FastAPI service support, and automatic query integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufulin](https://clawhub.ai/user/wufulin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to index local PDF, Word, Excel, Markdown, and text documents, then retrieve source-grounded answer snippets through command-line queries or a local FastAPI service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Indexed private documents may be exposed through the local retrieval interface. <br>
Mitigation: Index only documents appropriate for the deployment environment, avoid adding secrets or highly sensitive files, and treat vector stores and BM25 indexes as sensitive local data. <br>
Risk: The FastAPI service is described as unauthenticated and may bind to all network interfaces. <br>
Mitigation: Bind the service to 127.0.0.1 unless network access is intentional, and add authentication or network controls before exposing it beyond the local machine. <br>
Risk: Dependency and index-loading patterns require review before production use. <br>
Mitigation: Upgrade and lock dependencies, review generated indexes before reuse, and follow the security guidance from the server scan before production deployment. <br>


## Reference(s): <br>
- [System Architecture](references/system_architecture.md) <br>
- [Hybrid Search](references/hybrid_search.md) <br>
- [FastAPI Service](references/fastapi_service.md) <br>
- [Hybrid Search Testing](references/hybrid_search_testing.md) <br>
- [PDF Reading](references/pdf_reading.md) <br>
- [Excel Reading](references/excel_reading.md) <br>
- [Excel Analysis](references/excel_analysis.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with command examples, configuration snippets, and retrieved source excerpts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include document source names, chunk identifiers, retrieval scores, and truncated content snippets.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
