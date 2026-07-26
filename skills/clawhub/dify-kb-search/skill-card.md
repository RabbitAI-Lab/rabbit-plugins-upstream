## Description: <br>
Search Dify Knowledge Base (Dataset) to get accurate context for RAG-enhanced answers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiaowenzhou](https://clawhub.ai/user/xiaowenzhou) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to list and search Dify knowledge base datasets for retrieval-augmented context in question answering, documentation lookup, and contextual response workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and retrieved context are sent to the configured Dify instance using DIFY_API_KEY. <br>
Mitigation: Use a least-privileged Dify key, prefer approved HTTPS endpoints, and avoid sending secrets or regulated data unless that Dify environment is approved. <br>
Risk: Results depend on the trustworthiness and availability of the configured Dify endpoint. <br>
Mitigation: Install only for Dify instances you trust and verify DIFY_BASE_URL before use. <br>


## Reference(s): <br>
- [Dify API Reference](https://docs.dify.ai/reference/api-reference) <br>
- [ClawHub Skill Page](https://clawhub.ai/xiaowenzhou/skills/dify-kb-search) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, API Calls, Guidance] <br>
**Output Format:** [JSON responses containing dataset lists or retrieved knowledge-base chunks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DIFY_API_KEY and DIFY_BASE_URL; search supports dataset_id, top_k, search_method, and reranking_enable.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
