## Description:

Search MuseScore sheet music and read score metadata via MCP. Triggers on phrases like "find sheet music for", "search MuseScore for", "is there a free arrangement of", "what's the license on this MuseScore score", "how many pages is", or any request involving MuseScore scores, arrangements, or sheet-music metadata. Requires musescore-mcp installed and the ContextMint Bridge browser extension active with a signed-in musescore.com tab (see Setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Musicians and music researchers can search MuseScore for arrangements and inspect score details such as composer, instrumentation, license, key, and duration. They can request available score files or PDF conversions when their MuseScore access permits it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a signed-in browser session and browser extension to access MuseScore.

Mitigation: Review the MCP implementation and extension permissions before installation, and approve only the MuseScore access you need.

Risk: Despite its Read-only label, the skill can create or move local files.

Mitigation: Choose download destinations deliberately and review file operations before allowing them.

## Reference(s):

- [MuseScore](https://musescore.com)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Text, Structured data, Files]

**Output Format:** [Text and structured score metadata, links, and available score files or PDF output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Score availability and file delivery depend on MuseScore access; PDF results can be partial or gated.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
