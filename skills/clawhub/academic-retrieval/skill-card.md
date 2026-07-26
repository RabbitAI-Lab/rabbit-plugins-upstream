## Description: <br>
Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and byte-range content reading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sciverse](https://clawhub.ai/user/sciverse) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and external agent users use this skill to locate academic papers, retrieve metadata and semantic excerpts, read accessible full text ranges, and fetch referenced paper figures or table images for citation-grounded workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries, requested document identifiers, and the Sciverse API token are sent to Sciverse. <br>
Mitigation: Install only when Sciverse academic retrieval is intended, keep the token scoped to this service, and avoid using SCIVERSE_BASE_URL unless it points to a trusted sciverse.space endpoint. <br>
Risk: Full-text reading may be unavailable for papers without accessible content or caller authorization. <br>
Mitigation: Check is_content_accessible before calling read_content and fall back to metadata or semantic search results when full text cannot be read. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval) <br>
- [Sciverse homepage](https://sciverse.space) <br>
- [Sciverse API endpoint](https://api.sciverse.space) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands] <br>
**Output Format:** [JSON responses and Markdown text fragments, with shell command examples for direct invocation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; read_content only works when full text is available and authorized.] <br>

## Skill Version(s): <br>
0.9.0 (source: SKILL.md frontmatter, manifest.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
