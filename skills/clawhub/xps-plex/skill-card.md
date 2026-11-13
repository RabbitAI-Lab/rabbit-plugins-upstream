## Description:

Project a web page fullscreen onto the second laptop (ssh host `xps`) over SSH: start the v2rayN proxy if it is down, launch Firefox or Brave on a dedicated proxy profile, park the proxy GUI on its own workspace, fullscreen the page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Users who want to check a second laptop's proxy or browser state, or show a requested page, stream, or Plex live TV on its display, can use this skill to inspect the state and open the page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser actions may disrupt an unrelated session, remove recoverable session data, or show personal content on the projected display.

Mitigation: Check the remote browser state and window titles before opening a page, preserve any session data you need, and confirm the target page is appropriate for the display.

Risk: The security review is incomplete because a local path-like reference in SKILL.md could not be resolved.

Mitigation: Treat the scan as incomplete and review the unresolved reference before relying on the skill.

## Reference(s):

- [Projecting a Tab Onto Another Machine](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261110-projecting-a-tab-onto-another-machine.md)
- [A Skill or an MCP Server?](https://github.com/j3ffyang/ai-thoughts/blob/main/docs/261111-skill-vs-mcp.md)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Configuration]

**Output Format:** [Shell commands and key-value status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Status reports include proxy state, browser counts, window titles, launch or reuse action, and fullscreen mode.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
