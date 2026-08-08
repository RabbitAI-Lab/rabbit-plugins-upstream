## Description:

Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and byte-range content reading. For agent workflows that need citation-grade scientific literature.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and agents use this skill to locate academic papers by structured criteria, retrieve semantically relevant paper chunks for citation-grounded answers, and expand context from known document IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Academic search queries, paper IDs, filters, and content or resource requests are sent to Sciverse using SCIVERSE_API_TOKEN.

Mitigation: Use the skill only when transmitting that information to Sciverse is intended, and do not include unrelated credentials or sensitive private text in tool arguments.

Risk: Semantic retrieval and scoped filtering can return partial or approximate context, including chunks with missing metadata.

Mitigation: Use read_content to inspect surrounding source text before relying on an excerpt, and avoid presenting soft-filtered results as a hard corpus guarantee.

## Reference(s):

- [Sciverse](https://sciverse.space)
- [ClawHub Skill Page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [JSON responses containing paper metadata, semantic text chunks, Markdown content fragments, or base64-encoded image resources.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCIVERSE_API_TOKEN. Optional SCIVERSE_BASE_URL is constrained to sciverse.space domains by the artifact scripts.]

## Skill Version(s):

0.13.1 (source: SKILL.md frontmatter, manifest.json, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
