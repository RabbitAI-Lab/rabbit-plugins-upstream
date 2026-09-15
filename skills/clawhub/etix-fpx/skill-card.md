## Description:

Query etix.com event ticketing from a shell with the fpx CLI instead of running the etix-mcp server, including event, venue, and performer search plus event and venue detail through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover public Etix event, venue, and performer data from shell workflows when an MCP server is not installed or desired. It helps resolve names to numeric Etix IDs, fetch detail pages, parse JSON or HTML-derived event data, and troubleshoot fetchproxy bridge failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing the fpx CLI and may optionally install parsing dependencies for local HTML extraction.

Mitigation: Use pinned package versions where practical, avoid sudo for npm installs, and review installed packages before deployment.

Risk: Pairing the browser bridge allows fpx to issue Etix-domain requests through the user's browser profile until the pairing is removed.

Mitigation: Pair only in an intended browser profile, limit Chrome site access to etix.com, and remove the pairing when it is no longer needed.

Risk: HTML responses can still be DataDome interstitial pages even when the fetch command exits successfully.

Mitigation: Check fetched HTML for captcha-delivery or the documented blocker message before parsing event or venue detail.

Risk: The skill intentionally excludes ticket purchasing and seller APIs because those involve financial action or venue credentials.

Mitigation: Keep usage limited to anonymous public discovery reads and do not use the skill to buy tickets or access credentialed seller endpoints.

## Reference(s):

- [Etix consumer endpoints for fpx](references/etix-endpoints.md)
- [extract-datalayer.mjs](references/extract-datalayer.mjs)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/etix-fpx)
- [Third-party publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, jq, and Node.js command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one-shot fpx requests, setup commands, parsing snippets, endpoint cautions, and troubleshooting steps.]

## Skill Version(s):

0.6.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
