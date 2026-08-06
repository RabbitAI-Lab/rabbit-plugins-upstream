## Description:

Sciverse Academic Retrieval helps agents search academic paper metadata, retrieve semantic chunks for RAG, and read byte-range content for citation-grade scientific literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and external agent users use this skill to ground research workflows in academic paper metadata, semantic search chunks, and source text excerpts. It is suited for literature discovery, RAG citation support, DOI lookup, citation or reference exploration, and figure retrieval when content references images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, filters, document identifiers, and content or figure requests are sent to Sciverse.

Mitigation: Do not include secrets, regulated data, or confidential proprietary research context unless the Sciverse account and organizational policy allow it.

Risk: The skill requires a Sciverse API token for requests.

Mitigation: Provide the token through the documented environment variable and avoid exposing it in prompts, logs, or shared command examples.

Risk: Full-text access depends on paper availability and caller authorization.

Mitigation: Check accessibility fields before requesting content and verify cited excerpts against returned source text.

## Reference(s):

- [Sciverse](https://sciverse.space)
- [ClawHub Skill Page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [Publisher Profile](https://clawhub.ai/user/sciverse)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [JSON responses with paper metadata, semantic search chunks, byte-range text or Markdown fragments, and base64-encoded image resources when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Sciverse API token and may return only metadata when full text is unavailable or unauthorized.]

## Skill Version(s):

0.12.0 (source: frontmatter, manifest, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
