## Description: <br>
Search for physical products, hardware, AI tools, and APIs via the Orion Ad Protocol. Returns structured data (JSON) optimized for agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[celsojr2013](https://clawhub.ai/user/celsojr2013) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to find product offers, hardware, APIs, SaaS tools, libraries, and SDKs through OrionAds instead of scraping web pages. Account registration, ad posting, balance checks, and nonzero bids should be reviewed before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and ad or account payloads may be sent to OrionAds. <br>
Mitigation: Install only if this data sharing is acceptable, and avoid providing ORION_API_KEY unless account features are intended. <br>
Risk: Account registration, ad posting, or nonzero bids can create account or spending-impacting actions. <br>
Mitigation: Require explicit review before registering an account, posting an ad, or setting a nonzero bid. <br>
Risk: Unsafe shell construction could expose users to command injection when commands include user input. <br>
Mitigation: Use encoded query parameters for GET requests and escape or file-load JSON payloads for POST requests before execution. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/celsojr2013/skills/orionads) <br>
- [OrionAds search API](https://orionads.net/api/v1/search) <br>
- [OrionAds registration API](https://orionads.net/api/v1/register) <br>
- [OrionAds ads API](https://orionads.net/api/v1/ads) <br>
- [OrionAds account API](https://orionads.net/api/v1/me) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search is unauthenticated; account, ad posting, and balance actions may use ORION_API_KEY.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
