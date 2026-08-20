## Description:

Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and byte-range content reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and OpenClaw users use this skill to search academic paper metadata, retrieve semantically relevant paper chunks for RAG, inspect citation/reference relationships, and read authorized paper content for citation-grade scientific workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, paper identifiers, and retrieval requests are sent to Sciverse under the user's API token.

Mitigation: Use only where the organization approves Sciverse as a provider and avoid confidential, regulated, or proprietary research prompts unless that data flow is approved.

Risk: The skill depends on an API token and network access for retrieval.

Mitigation: Configure the token through the documented environment variable and review access controls before deployment.

## Reference(s):

- [Sciverse homepage](https://sciverse.space)
- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool responses and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; resource retrieval can return base64-encoded image bytes with a MIME type.]

## Skill Version(s):

0.14.0 (source: server evidence, frontmatter, and manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
