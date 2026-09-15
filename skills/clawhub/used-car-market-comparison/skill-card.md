## Description:

Compare used-car asking prices with matched local Crawlora listings to build a shortlist, estimate a comparable-listing range, or explain premiums and discounts by trim, mileage, condition, and location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect matched used-car listings from CarMax, Autotrader, and Cars.com through Crawlora, then compare advertised prices against a target vehicle or buyer requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends scoped vehicle search criteria and location information to Crawlora as a third-party API.

Mitigation: Send only the ZIP, location, and vehicle criteria needed for the comparison, and avoid unnecessary personal details.

Risk: Advertised listings can be stale, incomplete, duplicated, or different from final transaction terms.

Mitigation: Present results as advertised-listing evidence with retrieval dates, sample limits, exclusions, fee/history gaps, and seller follow-up questions.

Risk: A comparable-listing price range can be mistaken for a purchase valuation or out-the-door quote.

Mitigation: Keep taxes, registration, dealer fees, transfer fees, vehicle history, and mechanical condition separate unless explicitly documented.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/used-car-market-comparison)
- [ClawHub Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with comparison tables, price summaries, source links, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include retrieval dates, excluded-record notes, uncertain matches, fee/history gaps, and seller questions.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
