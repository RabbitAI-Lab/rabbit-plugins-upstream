## Description:

Sciverse academic paper retrieval supports structured metadata search, semantic chunk retrieval for RAG, citation relation lookup, and character-range content reading for scientific literature workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and research-focused agents use this skill to locate academic papers, retrieve grounded text snippets, inspect citation relationships, and fetch referenced figures or tables for literature review and RAG workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, document IDs, and resource names are sent to Sciverse endpoints with the user's API token.

Mitigation: Use a token approved for the intended workspace and avoid submitting confidential research prompts or identifiers unless Sciverse terms and internal policy allow it.

Risk: Retrieved chunks, full text, citation relations, and images can be permission-limited, partial, or approximate for citation-grade use.

Mitigation: Check content accessibility and verify important claims or citations against the source publication before relying on downstream answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [Sciverse homepage](https://sciverse.space)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, images, configuration]

**Output Format:** [JSON responses containing paper metadata, semantic chunks, Markdown text fragments, citation relation lists, or base64-encoded image resources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Sciverse API token; Node 18+ scripts call Sciverse endpoints and print machine-readable JSON.]

## Skill Version(s):

0.14.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
