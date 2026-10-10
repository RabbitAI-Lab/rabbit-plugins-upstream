## Description:

Search koopje.ai for Belgian second-hand deals and auctions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[antarcticaice](https://clawhub.ai/user/antarcticaice)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and agents search and compare Belgian second-hand listings and auction lots, inspect listing details, and optionally manage saved or owned listings with the user's permission.

### Deployment Geography for Use:

Global (search coverage focuses on Belgian listings)

## Known Risks and Mitigations:

Risk: Searches and location details are sent to koopje.ai using the user's API key.

Mitigation: Use only when the user intends to share the search and any provided location details with koopje.ai.

Risk: Saving, removing, renewing, or publishing listings can change the user's account or make an ad public.

Mitigation: Require an explicit request and final confirmation before each account-changing action, especially for public listings or precise coordinates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/antarcticaice/skills/koopje-search)
- [koopje.ai API documentation](https://koopje.ai/api)
- [Included API reference](references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown summaries with listing links and optional API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include available prices, locations, and original listing sources.]

## Skill Version(s):

1.0.17 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
