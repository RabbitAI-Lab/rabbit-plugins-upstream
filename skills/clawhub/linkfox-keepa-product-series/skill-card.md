## Description: <br>
Queries Amazon product history for a single ASIN, including price, Buy Box, BSR, ratings, seller count, and monthly sales time-series data across supported marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, Amazon sellers, and e-commerce analysts use this skill to retrieve and summarize historical product-level Keepa data for ASIN-specific price, ranking, rating, seller-count, and sales trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox receives API requests and session/app metadata when the skill calls the product-history endpoint. <br>
Mitigation: Use the skill only when sharing ASIN queries and runtime metadata with LinkFox is acceptable. <br>
Risk: Full Keepa API responses are persisted locally, including cached and session output files. <br>
Mitigation: Store outputs only in appropriate workspaces and periodically delete the local linkfox cache and session data when product research is sensitive. <br>
Risk: The onboarding fallback references an unpinned remote ZIP installer. <br>
Mitigation: Avoid remote onboarding installation unless the LinkFox source is separately trusted and reviewed. <br>
Risk: Historical trend lookups consume LinkFox/Keepa credits and may incur higher cost for broad requests. <br>
Mitigation: Confirm the requested ASIN, marketplace, days, and optional series before issuing additional calls. <br>


## Reference(s): <br>
- [Keepa Amazon Price History API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-series) <br>
- [LinkFox API Key and Credits Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Guidance, Analysis] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON or text summaries and human-readable trend guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries one ASIN per request, supports up to 365 days of history, uses a 24-hour local cache, and may consume LinkFox/Keepa credits.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
