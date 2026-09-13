## Description:

Compare short-term rental market supply, listing density, room mix, price distributions, and review signals using Crawlora Airbnb aggregates and selected live listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and market researchers use this skill to compare Airbnb short-term-rental markets with aggregate supply, density, room mix, price, and review signals while keeping live listing examples separate from market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected market, listing, and search parameters are sent to Crawlora with the user's API key.

Mitigation: Keep the API key in the environment, scope requests to the research objective and credit budget, and install only when this data sharing is acceptable.

Risk: Returned Airbnb data can be mistaken for legal, revenue, occupancy, or demand proof.

Mitigation: Treat results as sampled market evidence, preserve freshness and suppression limits, and avoid using listing density alone for investment, compliance, or revenue conclusions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/short-term-rental-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown market comparison with optional shell command snippets and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes collection dates, filter scope, suppression and enrichment limits, price basis, and separate sampled listing examples when used.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
