## Description:

Helps agents search U.S. homes.com listings, retrieve property details and history, and read a user's saved homes or searches through their signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to find U.S. property listings, look up addresses, and summarize listing details, photos, and history. With explicit permission, they can also retrieve a user's saved homes and searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and searches expose account-linked information from the signed-in browser session.

Mitigation: Fetch saved items only when the user explicitly asks; confirm the browser pairing and avoid sharing or retaining account-linked results unnecessarily.

Risk: Address lookup can return a nearby property rather than the requested address.

Mitigation: Check the selected property's street address against the requested address before presenting it as a match.

Risk: Fetching listings through a signed-in browser session may exceed the user's intended site usage.

Mitigation: Keep requests within homes.com's terms and use the paired session only with the user's consent.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [homes.com](https://www.homes.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and structured property data examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property results may include listing links, photos, prices, and history; saved items are account-linked.]

## Skill Version(s):

2.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
