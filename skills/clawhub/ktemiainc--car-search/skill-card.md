## Description:

Search and compare rental cars through the Ktemia API, returning each seller's price and booking link for specified trips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers use the skill to compare rental cars for a specified pickup location and date range, refine results by seller or agency, and open a selected seller's booking page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches use a required API key to make requests to the external Ktemia car API, and each request uses the user's quota.

Mitigation: Provide the API key only if comfortable sending searches to Ktemia, and consider quota use before starting additional searches.

Risk: The security scan was partial because some local references were unresolved, so its evidence is incomplete.

Mitigation: Review the unresolved references before relying on the benign scan verdict.

## Reference(s):

- [Ktemia Car Search API](https://www.ktemia.com/docs/api/cars/search/)
- [Ktemia API Authentication](https://www.ktemia.com/docs/api/#authentication)
- [Ktemia API Errors](https://www.ktemia.com/docs/api/#errors)

## Skill Output:

**Output Type(s):** [Text, URLs]

**Output Format:** [Concise rental-car comparisons listing vehicles, prices, and seller booking links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices can change after search; booking takes place on the seller's site.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
