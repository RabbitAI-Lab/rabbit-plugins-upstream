## Description: <br>
Backend retrieval skill for structured search of occupational health standards and documents, returning relevant text with source and clause details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loda666](https://clawhub.ai/user/loda666) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this backend retrieval component to query a local vector knowledge base for occupational health regulations and return source-grounded text snippets. It is intended for agent workflows rather than direct end-user invocation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on unreviewed local RAG code and does not clearly disclose where user queries are processed. <br>
Mitigation: Install only when the local rag_system directory is controlled and trusted; review search_pipeline.py and embedding_client.py, confirm whether Qwen embedding or rerank calls leave the machine, and avoid sensitive queries unless that data flow is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/loda666/skills/rag-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance] <br>
**Output Format:** [JSON object containing ranked retrieval results with content, source, clause, regulation level, score, query, count, method, and error fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are controlled by the query and top_k inputs; default top_k is 5.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
