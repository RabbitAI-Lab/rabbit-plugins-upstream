## Description:

Search Etix events, venues, and performers and pull event and venue details via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to configure and operate an Etix MCP integration for natural-language discovery of Etix events, venues, performers, showtimes, and event details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration routes Etix requests through the user's browser session and a third-party browser extension.

Mitigation: Install only after reviewing the referenced projects, keep the extension limited to the intended Etix workflow, and approve pairing only for expected use.

Risk: The artifact states the project is unofficial, uses Etix website endpoints and pages, and should be used at the user's discretion.

Mitigation: Use it consistently with Etix's terms and expect Etix site behavior or endpoints to change without notice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix)
- [etix-mcp npm package](https://www.npmjs.com/package/etix-mcp)
- [etix-mcp source repository](https://github.com/chrischall/etix-mcp)
- [fetchproxy source repository](https://github.com/chrischall/fetchproxy)
- [Etix ticket site](https://www.etix.com/ticket/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires etix-mcp, the fetchproxy browser extension, and an open etix.com browser tab.]

## Skill Version(s):

0.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
