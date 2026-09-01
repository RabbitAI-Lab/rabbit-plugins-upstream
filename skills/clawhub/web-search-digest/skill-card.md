## Description:

Search the web on a topic and produce a structured markdown digest summarizing key findings with source references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research a topic, summarize recent findings, and collect source-backed references in a structured digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated summaries may be incomplete or may misrepresent fetched source content.

Mitigation: Review the digest against the cited sources before using it for important decisions.

Risk: The skill can create a markdown digest file in the workspace when explicitly requested.

Mitigation: Only request file output when a workspace artifact is intended, and review the generated file before reuse.

## Reference(s):

- [Web Search Digest ClawHub page](https://clawhub.ai/terrycarter1985/skills/web-search-digest)

## Skill Output:

**Output Type(s):** [text, markdown, files]

**Output Format:** [Markdown digest with key findings, per-source summaries, source links, and gaps or open questions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sources consulted count; writes a workspace markdown digest only when the user asks for a file.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
