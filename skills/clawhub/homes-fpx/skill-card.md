## Description:

Query Homes.com from a shell with the fpx CLI to search listings, resolve street addresses, fetch property details, photos, history, and access the signed-in user's saved homes through their own browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to make one-shot Homes.com requests through fpx when they need listing search, property detail, saved-home, saved-search, or address-resolution data without running the homes-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in Homes.com browser session, including optional access to saved homes and saved searches.

Mitigation: Install only if that session access is acceptable; use a separate browser profile or sign out when account-specific pages should not be exposed.

Risk: Homes.com requests may return a sign-in redirect, AWS WAF challenge page, or changed HTML shape instead of expected listing data.

Mitigation: Check response bodies and fpx exit codes, confirm the paired browser tab is signed in and past the WAF challenge, and review extracted data before relying on it.

Risk: Free-text address resolution can return the closest result rather than a confirmed property match.

Mitigation: Resolve addresses through the documented typeahead, slug, and search fallback order, then verify the selected candidate against the requested address.

## Reference(s):

- [homes.com request recipes](artifact/references/homes-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/homes-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, JavaScript, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces request recipes and extraction guidance for use with fpx, a paired browser tab, node, and jq.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
