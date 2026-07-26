## Description: <br>
Search and compare grocery prices and promotions in Austria and Germany via the Preisrunter API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davidus05](https://clawhub.ai/user/davidus05) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and shopping-focused agents use this skill to find grocery prices, promotions, sale items, and shop-specific product links for Austria and Germany. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Grocery search terms, region choices, and shop filters are sent to the external Preisrunter API. <br>
Mitigation: Avoid personal details, addresses, account data, and sensitive context in searches. <br>
Risk: Malformed query parameters can change or break API requests. <br>
Mitigation: URL-encode query and shop parameters before running curl commands. <br>
Risk: The upstream API may rate-limit frequent requests. <br>
Mitigation: Avoid aggressive polling and handle HTTP 429 responses gracefully. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/davidus05/skills/preisrunter) <br>
- [Preisrunter homepage](https://preisrunter.at) <br>
- [Preisrunter OpenClaw products API](https://api.preisrunter.net/wrapper/openclaw-v1/products/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with curl and jq command examples plus product result fields and source links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; search queries, region choices, sale filters, and shop filters are sent to the external Preisrunter API.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
