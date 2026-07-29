## Description: <br>
Retrieve academic papers by structured metadata, run semantic chunk search for RAG, and read byte-range content for citation-grade scientific literature. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciverse](https://clawhub.ai/user/sciverse) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and agents use this skill to find scholarly papers, retrieve relevant text chunks for grounded answers, inspect paper metadata and relations, and fetch figure or table resources when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Academic search queries, lookup parameters, and paper access requests are sent to Sciverse with the configured API token. <br>
Mitigation: Install only where this external retrieval is acceptable, protect SCIVERSE_API_TOKEN, and avoid sending sensitive or confidential research queries unless authorized. <br>
Risk: Retrieved excerpts, relation counts, and citation lists can be incomplete, permission-limited, or capped for very large citation sets. <br>
Mitigation: Check content accessibility before reading full text, follow documented paging limits, and verify citation-grade claims against the returned source metadata and excerpts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sciverse/skills/academic-retrieval) <br>
- [Sciverse](https://sciverse.space) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, binary image data, guidance] <br>
**Output Format:** [JSON tool responses containing paper metadata, semantic chunks, text fragments, relation lists, catalog fields, or base64-encoded image resources.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; SCIVERSE_BASE_URL may only target sciverse.space domains.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release evidence and skill manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
