## Description:

Helps agents search and analyze bidding notices, companies, suppliers, competitors, and procurement market trends using the 知了标讯 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use the skill to find Chinese tender and award notices, investigate companies and potential suppliers, and analyze purchasing activity and prices. It requires access to the third-party 知了标讯 service and an API key.

### Deployment Geography for Use:

Global (service data focuses on Chinese bidding and company records)

## Known Risks and Mitigations:

Risk: Third-party service receives bidding and company queries together with API-key-authenticated requests and package identity information.

Mitigation: Avoid sending sensitive queries unless this disclosure is acceptable; use a trusted secret mechanism for the API key.

Risk: Optional automatic registration sends a hashed device identifier and saves an API key locally.

Mitigation: Prefer manually configuring an API key; obtain consent before registration and review local storage at ~/.zlbx/config.json.

Risk: Account checks and update acknowledgments can contact the service beyond the user's requested data query.

Mitigation: Review these service interactions before installation, especially when restricting outbound requests.

Risk: Contact-search features can expose personal contact information or enable unwanted outreach.

Mitigation: Avoid bulk outreach and sensitive personal-data collection; respect masked contact details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [Bidding search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Company registry interpretation guide](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration guide](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with tables and cited bidding records where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the service's available records, API-key access, and account credits; contact details may be masked for trial accounts.]

## Skill Version(s):

1.4.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
