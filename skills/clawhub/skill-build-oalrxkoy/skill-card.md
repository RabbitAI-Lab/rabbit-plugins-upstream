## Description:

This MCP server lets an AI assistant retrieve OPC discovery and AI tools articles for solo entrepreneurs using a personal OPC API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers connect the MCP server to Claude Desktop, Cursor, or Cline to ask for recent OPC discovery articles, AI tool recommendations, and productivity content without browsing manually.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Every tool result includes the publisher's promotional footer and link.

Mitigation: Install only if the promotional footer is acceptable for the intended environment, or ask the publisher to remove it before deployment.

Risk: The skill requires a personal OPC API key.

Mitigation: Store OPC_API_KEY only in client secret configuration, do not commit configs containing the key, and reset the key immediately if it is exposed.

Risk: The server-side provenance source is unavailable for this release.

Mitigation: Do not rely on inferred GitHub provenance; review the ClawHub release evidence and artifact files directly before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-oalrxkoy)
- [OPC service site](https://mrkjai.com)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [MCP text responses, usually Markdown-formatted lists with article titles, summaries, categories, authors, dates, and links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPC_API_KEY; optional filters include type, featured, and limit.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter, package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
