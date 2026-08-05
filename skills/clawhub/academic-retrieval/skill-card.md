## Description:

Retrieve academic papers by structured metadata, perform semantic chunk search for RAG, and read byte-range content for citation-grade scientific literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agent users use this skill to locate academic papers, retrieve citation-oriented paper metadata, perform semantic chunk retrieval for RAG, and expand selected chunks into byte-range excerpts or referenced figure resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents query Sciverse using SCIVERSE_API_TOKEN, so an overly broad or exposed token could be misused.

Mitigation: Install only for workflows that need Sciverse access, keep the token private and scoped, and avoid printing or sharing it.

Risk: Returned paper text and images are external content and may be incomplete, inaccessible, or misleading if used without verification.

Mitigation: Treat returned content as source material, verify citations against the original papers, and check content accessibility before expanding excerpts.

## Reference(s):

- [Sciverse homepage](https://sciverse.space)
- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [JSON responses containing paper metadata, text excerpts, Markdown fragments, and base64-encoded image resources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN; optional SCIVERSE_BASE_URL is restricted to sciverse.space domains.]

## Skill Version(s):

0.11.1 (source: release evidence, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
