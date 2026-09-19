## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve addresses, fetch property details, photos, and history, and read a signed-in user's saved homes through their own browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to retrieve homes.com listing, property-detail, market, saved-home, and saved-search data from shell workflows without running the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches can expose account-specific homes.com data from the user's signed-in browser session.

Mitigation: Use a separate browser profile or sign out before running auth-gated commands when account-specific data should not appear in agent output.

Risk: Homes.com may return sign-in redirects, WAF challenge pages, or closest-match property results instead of the intended listing.

Mitigation: Check responses for sign-in or WAF challenge markers and verify resolved property candidates against the requested address before using the data.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, jq, and Node.js code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a paired Transporter browser extension and a signed-in homes.com tab for saved homes or saved searches.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
