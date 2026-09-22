## Description:

homes-fpx helps agents query homes.com from a shell through the fpx CLI, using a signed-in browser session to search listings, resolve addresses, fetch property details, photos, history, nearby listings, and saved homes or saved searches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve homes.com listing and property information from shell workflows when the MCP server is unavailable or unnecessary. It is useful for scripted real-estate search, address resolution, property detail review, and deliberate access to the user's saved homes or saved searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches can reveal private housing preferences and search behavior.

Mitigation: Ask the agent to fetch saved homes or saved searches only when needed, avoid unnecessary retention, and delete temporary raw HTML or JSON files after use.

Risk: The skill relies on the user's own signed-in browser session and Transporter pairing.

Mitigation: Use it only with an account and browser session the user intends to expose to the agent, and confirm the paired tab is connected before requesting account-gated pages.

Risk: homes.com may return redirects, WAF challenge pages, or closest-match address results rather than confirmed property matches.

Mitigation: Check response bodies for sign-in or WAF challenge pages and verify resolved property candidates against the requested address before using the result.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub homes-fpx release page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON extraction examples, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may write temporary HTML or JSON files under /tmp; saved-home and saved-search examples require a signed-in homes.com browser tab.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
