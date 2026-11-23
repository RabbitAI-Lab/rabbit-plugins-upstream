## Description:

Turns an X or Twitter post link into readable post text, text found in images, and video transcripts for an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People using an AI agent can provide an X or Twitter post link to get its text, image text, or video transcript for reading, summarizing, or rewriting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The medium-confidence security review flags possible credential flow and missing tool-scope declarations.

Mitigation: Review how LINKDIGEST_API_KEY is handled and limit the runtime's network and tool permissions to the needs of this skill.

Risk: Skillspector reported possible undeclared extra features; its findings have some uncertainty.

Mitigation: Review the skill's documented capabilities and behavior before enabling it.

## Reference(s):

- [LinkDigest X platform guide](https://linkdigest.dev/platforms/x?ref=skill-twitter-to-text)
- [LinkDigest MCP server](https://linkdigest.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the post author and date, image text, and video transcript when available; full output requires an optional API key.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
