## Description:

tock-mcp helps agents discover Tock restaurants, inspect venue details, bookable experiences, prices, party sizes, open dates and times, and read signed-in account reservation/profile data through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent find Tock cities and restaurants, inspect venue availability, and verify account reservations while leaving booking and payment on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release relies on an unpinned MCP package and browser extension code.

Mitigation: Pin and review the package version or commit before installing, and inspect the extension permissions.

Risk: Account tools depend on a persistent bridge to a signed-in Tock browser session.

Mitigation: Use account tools only in a trusted browser profile and understand how to revoke the browser pairing.

Risk: The skill depends on Tock web pages and browser challenge behavior rather than an official consumer API.

Mitigation: Treat availability and reservation results as advisory and verify final booking or account state directly on Tock.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples; MCP tool results are structured text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only. Account tools require a signed-in exploretock.com tab and the fetchproxy browser extension.]

## Skill Version(s):

0.5.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
