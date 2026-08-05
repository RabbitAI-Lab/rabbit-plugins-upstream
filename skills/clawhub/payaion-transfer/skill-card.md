## Description: <br>
Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jan-blockbites](https://clawhub.ai/user/jan-blockbites) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to upload files through Payaion, share download links, browse marketplace listings, and optionally publish paid file listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploads and marketplace listings can expose selected files publicly. <br>
Mitigation: Confirm that each file is appropriate to upload or list before running the transfer flow, and avoid sensitive directories unless the user explicitly approves. <br>
Risk: Paid listings use real USDC settlement on Base mainnet. <br>
Mitigation: Verify the per-download price with the user before publishing a paid marketplace listing. <br>
Risk: The skill requires a Payaion API key. <br>
Mitigation: Install and use the skill only when sharing PAYAION_API_KEY with Payaion is acceptable, and check authorization errors before retrying. <br>


## Reference(s): <br>
- [Payaion Homepage](https://payaion.com) <br>
- [Payaion Documentation](https://payaion.com/docs) <br>
- [Payaion OpenAPI Specification](https://payaion.com/openapi.yaml) <br>
- [Payaion Plans and Pricing](https://payaion.com/pricing) <br>
- [ClawHub Skill Listing](https://clawhub.ai/jan-blockbites/skills/payaion-transfer) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown with curl commands and JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and PAYAION_API_KEY; paid marketplace listings settle in USDC on Base mainnet.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
