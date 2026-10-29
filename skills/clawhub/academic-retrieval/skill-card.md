## Description:

Sciverse academic paper retrieval: structured metadata search, semantic chunk retrieval for RAG, and character-range content reading (offsets in Unicode code points).

This skill is ready for commercial/non-commercial use.

## Publisher:

[sciverse](https://clawhub.ai/user/sciverse)

### License/Terms of Use:

Apache-2.0

## Use Case:

Researchers and developers use the skill to find academic papers by structured criteria, retrieve relevant passages for evidence-grounded answers, and read selected portions of paper text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search text and filters are sent to Sciverse.

Mitigation: Avoid submitting confidential research or personal information without authorization, protect the SCIVERSE_API_TOKEN, and retain the default HTTPS endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sciverse/skills/academic-retrieval)
- [Sciverse](https://sciverse.space)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [JSON containing paper metadata, ranked text chunks, or requested text ranges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested search or content range and require Sciverse API access.]

## Skill Version(s):

0.15.1 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
