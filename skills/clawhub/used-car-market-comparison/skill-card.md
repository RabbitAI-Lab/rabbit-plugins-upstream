## Description:

Compare used-car asking prices with matched local listings through Crawlora. Use for a vehicle shortlist, a comparable-listing price range, or explaining a listing's premium or discount by trim, mileage, condition, and location.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External buyers, sellers, and agents use this skill to collect comparable used-car listings from CarMax, Autotrader, and Cars.com, then explain a target listing's advertised price range, premium, discount, and evidence gaps.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The Crawlora API key could be sent to an environment-selected API base.

Mitigation: Run the helper only where CRAWLORA_API_BASE cannot be tampered with, or validate that the API base is https://api.crawlora.net/api/v1 before use.

Risk: Used-car search parameters may contain sensitive personal data such as location or buyer requirements.

Mitigation: Use a low-privilege Crawlora key and avoid sending sensitive personal data in search parameters.

Risk: The bundled helper can call paths broader than the documented used-car endpoints.

Mitigation: Restrict helper use to the documented vehicle endpoints in artifact/reference/endpoints.md.

Risk: Advertised listings can support comparison but cannot establish transaction value, sale speed, or mechanical condition.

Mitigation: Present price outputs as advertised-listing comparisons, keep fee and history gaps visible, and avoid precise valuation claims for small or poorly matched samples.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/used-car-market-comparison)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown with comparable-listing tables, price summaries, evidence notes, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora JSON responses; should include source URLs, retrieval dates, excluded records, uncertain matches, and fee/history gaps.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
