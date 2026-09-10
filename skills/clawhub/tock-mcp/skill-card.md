## Description:

Discover restaurants on Tock through MCP, including metros, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in account reservation checks when the browser bridge is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an MCP-capable agent to Tock restaurant discovery and availability workflows. It can help find venues, inspect experiences and open times, review signed-in account reservations, and verify booking outcomes after the user completes booking on Tock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup runs a third-party npm MCP package and depends on a browser extension connected to a signed-in Tock tab.

Mitigation: Install only from a trusted publisher, pin to a reviewed exact package version where possible, inspect extension permissions, and approve pairing only for the expected identity.

Risk: The browser bridge can access signed-in Tock account context for profile, reservation, and verification tools.

Mitigation: Use a dedicated or trusted browser profile, limit use to necessary Tock workflows, and revoke the browser pairing when the integration is no longer needed.

Risk: Tock booking is completed outside the skill, and immediate post-booking signals may be inconclusive.

Mitigation: Treat a booking as attempted until confirmation evidence is captured and the reservation verification tool reports a confirmed result after any account-data lag.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with MCP tool calls, JSON configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Tock discovery and account-status outputs; compact and full views are available for selected restaurant and profile tools.]

## Skill Version(s):

0.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
