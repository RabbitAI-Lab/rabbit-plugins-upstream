## Description:

Search and compare hotels with the Ktemia hotel API and return each seller's price, a booking link, and guest reviews. Use when the user asks to find, compare, or price a stay in a city on specific dates, to narrow prices to one booking site, or to read reviews of a hotel. Asks for missing details instead of guessing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

Travelers use an agent to compare hotel prices and booking options for a confirmed destination and stay, and to review guest feedback before choosing where to book.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches send the user's API key and trip details to Ktemia's external hotel API.

Mitigation: Use the API key only if the user trusts Ktemia with it and the search details; keep the key in the configured environment variable and review the host runtime's network access.

Risk: The security review reports incomplete scanner coverage, so its benign verdict does not cover every behavior or dependency.

Mitigation: Review the skill and its host environment before use, especially where API credentials or travel details are sensitive.

## Reference(s):

- [Ktemia hotel search API documentation](https://www.ktemia.com/docs/api/hotels/search/)
- [Ktemia API authentication](https://www.ktemia.com/docs/api/#authentication)
- [Ktemia API errors](https://www.ktemia.com/docs/api/#errors)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown hotel comparisons with prices, seller booking links, and guest review excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices and availability can change; bookings are completed on the seller's site.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
