## Description:

Travel Search RU helps agents search Russian-catalog package tours, hotels, flights, trains, excursions, prices, and booking links for trip planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[missial](https://clawhub.ai/user/missial)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill as a search layer for travel planning when live Russian-catalog results are needed for package tours, hotel-only stays, flights, trains, activities, destination directories, prices, and booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trip criteria are sent to an external travel service.

Mitigation: Do not include names, contact details, passport or payment data, credentials, or unnecessary sensitive information in search criteria.

Risk: Search results can contain cached, indicative, or incomplete provider data.

Mitigation: Treat results as search assistance and verify provider coverage, availability, seats, final prices, and booking terms before purchase.

## Reference(s):

- [Travel Search CLI usage](references/usage.md)
- [ClawHub release page](https://clawhub.ai/missial/skills/travel-search-ru)
- [Production MCP endpoint](https://mcp.botclaw.ru/travel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON search results from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill returns travel search assistance only; final availability, prices, seats, and booking terms must be verified with the provider before purchase.]

## Skill Version(s):

2.2.0 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
