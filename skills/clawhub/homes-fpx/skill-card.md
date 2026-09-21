## Description:

Query homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, history, and read a signed-in user's saved homes through their own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query homes.com listing, property, market, and saved-home data from a shell when they want one-shot commands instead of the homes MCP server. It is useful for scripted real-estate lookups that run through the user's own signed-in browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access saved homes and saved searches through the user's signed-in homes.com browser session.

Mitigation: Use saved-home and saved-search recipes only on direct request, and avoid storing or sharing the resulting files unless needed.

Risk: Pairing fpx/Transporter with a signed-in homes.com tab allows shell commands to make requests as that browser session.

Mitigation: Install and pair the tool only when the user is comfortable with that access model, and keep the paired tab under the user's control.

Risk: homes.com can return redirects, WAF challenges, empty JSON-LD, or closest-match address results that look superficially successful.

Mitigation: Check response bodies, retry after clearing sign-in or WAF challenges, and verify resolved address candidates against the requested address before using detail data.

## Reference(s):

- [homes.com request recipes](artifact/references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and parsing recipes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fpx, the Transporter browser extension, jq, Node.js, and a paired homes.com browser tab for the documented recipes.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
