## Description:

Search and compare rental cars for specified locations and dates, returning seller prices and booking links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to search rental cars for specified pickup locations and dates, compare seller prices, and open booking links on the seller's site.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an environment variable and contacts an external API.

Mitigation: Before installing, review the external API use and confirm you are comfortable providing a Ktemia API key.

Risk: The security review is incomplete because some references could not be fully resolved.

Mitigation: Review unresolved references and the skill's behavior before installing.

## Reference(s):

- [Ktemia car search API](https://www.ktemia.com/docs/api/cars/search/)
- [Ktemia API authentication](https://www.ktemia.com/docs/api/#authentication)
- [Ktemia API errors](https://www.ktemia.com/docs/api/#errors)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [A concise comparison of rental cars, prices, sellers, and booking links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and booking links are returned by sellers; the skill does not reserve a car.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
