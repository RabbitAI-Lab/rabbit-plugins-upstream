## Description:

Search and compare hotels with the Ktemia hotel API and return each seller's price, a booking link, and guest reviews. Use when the user asks to find, compare, or price a stay in a city on specific dates, to narrow prices to one booking site, or to read reviews of a hotel. Asks for missing details instead of guessing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ktemiainc](https://clawhub.ai/user/ktemiainc)

### License/Terms of Use:

MIT-0

## Use Case:

External travelers use the skill to find and compare hotel stays for specified destinations and dates, filter results by booking site, and review hotel feedback. It returns seller booking links; the traveler completes the reservation with the seller.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hotel searches send request details to the external Ktemia API, and the client uses an API key from the environment.

Mitigation: Use the key through the documented environment variable, keep it out of prompts and logs, and review the provider's terms before sending travel details. The bundled client restricts its API URL to HTTPS on ktemia.com and refuses redirects.

Risk: The security scan was partial and did not establish whether the host runtime restricts network or environment access.

Mitigation: Review unresolved local references and apply the host's normal controls for network access and secrets before installing or running the skill.

## Reference(s):

- [Ktemia Hotel Search API documentation](https://www.ktemia.com/docs/api/hotels/search/)
- [Ktemia API authentication](https://www.ktemia.com/docs/api/#authentication)
- [Ktemia API errors](https://www.ktemia.com/docs/api/#errors)

## Skill Output:

**Output Type(s):** [Text, JSON, Links]

**Output Format:** [Hotel search summaries with prices, seller booking links, and guest review details; JSON from the bundled command-line client]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes hotel names, ratings, locations, stay prices, booking options, and reviews when available. Prices may change and bookings are completed on seller websites.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
