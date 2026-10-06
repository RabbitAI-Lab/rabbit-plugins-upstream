## Description:

Finds and compares Slickdeals and RetailMeNot offers through Crawlora, highlighting deal conditions and expiry caveats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and research agents use this skill to shortlist posted deals, compare eligibility and price conditions, and identify what still needs checking at checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deal searches and merchant or deal URLs are sent to Crawlora.

Mitigation: Avoid secrets and private account information in queries; use Crawlora only if its data handling is acceptable.

Risk: Posted deals, community reports, and coupon snapshots may not match current checkout prices or eligibility.

Mitigation: Preserve source links and observation times, separate conditional savings, and verify availability and final terms with the merchant before acting.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/deal-discovery-research)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown ranked shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes merchant, offer conditions, source links, observation times, and unresolved checkout questions.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
