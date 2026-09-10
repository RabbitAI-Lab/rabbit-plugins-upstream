## Description:

Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and byte-range content reading. For agent workflows that need citation-grade scientific literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and external agent users use this skill to locate academic papers, retrieve citation-ready paper chunks, inspect citation relationships, and expand selected paper text for research-grounded answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic search queries, document IDs, and retrieval requests are sent to Sciverse as an external service.

Mitigation: Use the skill only when that data sharing is acceptable for the workflow and avoid sending sensitive or confidential research prompts.

Risk: A misconfigured or untrusted API endpoint could expose the Sciverse API token.

Mitigation: Keep SCIVERSE_BASE_URL at the default HTTPS Sciverse endpoint or a trusted HTTPS gateway, and rotate the token if it was ever used with an HTTP endpoint.

Risk: Retrieved paper excerpts may be partial or unavailable when full text is not accessible.

Mitigation: Check the returned accessibility fields and use read_content pagination around selected offsets before relying on excerpts for citations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [Sciverse homepage](https://sciverse.space)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool responses and base64-encoded image resources when figures or tables are fetched.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN. Retrieval calls send academic search queries, document IDs, relation requests, and content-range requests to Sciverse.]

## Skill Version(s):

0.14.1 (source: SKILL.md frontmatter, manifest.json, evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
