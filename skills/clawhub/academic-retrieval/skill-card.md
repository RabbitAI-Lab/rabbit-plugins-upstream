## Description:

Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and character-range content reading (offsets in Unicode code points). For agent workflows that need citation-grade scientific literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

External developers and agent builders use this skill to find academic papers, retrieve citation-ready paper chunks, inspect metadata schemas, paginate paper relations, and read source content around selected excerpts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic queries, filters, document identifiers, content ranges, resource references, and the API token are sent to Sciverse; a plaintext or untrusted base URL could expose sensitive usage data or credentials.

Mitigation: Use the default HTTPS endpoint or another HTTPS Sciverse endpoint only, avoid http:// overrides, and rotate the token if it may have been used over plaintext HTTP.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [Sciverse](https://sciverse.space)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, image data, guidance]

**Output Format:** [JSON tool responses with text or Markdown paper excerpts and base64-encoded image resources when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; SCIVERSE_BASE_URL is optional and should remain on an HTTPS Sciverse endpoint.]

## Skill Version(s):

0.14.2 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
