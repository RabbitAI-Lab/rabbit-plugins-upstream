## Description:

Control application UI through project-owned DCC-CUA for explicit DCC-CUA requests, including browsers and non-DCC apps, or DCC-MCP UI fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use DCC-CUA to route UI-control work through the project-owned DCC-CUA runtime, bind an exact target, perform scoped browser, desktop, or DCC host actions, and verify the final application state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can observe and act on application, browser, and desktop UI through the DCC-CUA host.

Mitigation: Confirm the exact target, grants, and any repair or install prompt before allowing UI observation or input.

Risk: UI actions can affect the wrong application or stale state if the bound process, window, tab, or session changes.

Mitigation: Bind one exact target with process ID and native window handle, refresh observations after state changes, and verify the destination state after each mutation.

Risk: Public evidence can expose unrelated local context such as usernames, internal paths, browser profile data, credentials, tokens, or unrelated window titles.

Mitigation: Keep public evidence limited to route identity, scoped target IDs, semantic deltas, counters, and failure reasons unless full images are needed for grounding.

## Reference(s):

- [Continuity, batching, and token budgets](references/CONTINUITY.md)
- [DCC-host route](references/DCC_HOST.md)
- [Browser and non-DCC route](references/BROWSER_AND_DESKTOP.md)
- [Source skill page](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline text and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exact target binding and state verification before UI-control actions are considered complete.]

## Skill Version(s):

0.19.106 (source: metadata.dcc-mcp.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
