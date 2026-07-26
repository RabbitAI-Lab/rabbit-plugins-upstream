## Description: <br>
Queries a TikTok Shop seller's EchoTik product list by sellerId and returns product titles, prices, sales and GMV metrics, ratings, reviews, commissions, listing dates, sales channels, and categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketers, and e-commerce analysts use this skill to inspect a known TikTok Shop store's active product catalog and compare product performance by sales, GMV, price, reviews, and commission rate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sellerId queries, API credentials, and session/application metadata to LinkFox services. <br>
Mitigation: Confirm this data sharing is acceptable before installation, keep the LinkFox API key in environment variables, and avoid placing credentials or sensitive seller context in prompts or logs. <br>
Risk: Calls consume LinkFox credits and repeated pagination or retries can increase cost. <br>
Mitigation: Confirm cost expectations before high-volume use, prefer the built-in cache for repeated identical queries, and ask before making extra paid calls. <br>
Risk: Full API responses are written locally, and scanner guidance notes review-worthy storage behavior. <br>
Mitigation: Run the skill from an appropriate writable workspace, review saved `linkfox/` response and cache files for sensitive data, and delete retained outputs when they are no longer needed. <br>
Risk: The artifact includes an automatic feedback API path that can transmit user feedback content to LinkFox. <br>
Mitigation: Review feedback content before sending it and avoid including secrets, private business data, or unrelated user context. <br>


## Reference(s): <br>
- [EchoTik seller product API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-seller-product) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Guidance] <br>
**Output Format:** [JSON response saved to a local file, with either full JSON or a concise stdout summary for large responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a sellerId and a LinkFox API key; pageSize must be a multiple of 10 up to 100; calls consume LinkFox credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
