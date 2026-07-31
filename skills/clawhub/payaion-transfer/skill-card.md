## Description: <br>
Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jan-blockbites](https://clawhub.ai/user/jan-blockbites) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw agents and developers use this skill to upload local files or URLs to Payaion, share download links, and optionally publish paid marketplace listings with USDC per-download pricing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload local files or URL contents to Payaion, including sensitive files if the user selects them. <br>
Mitigation: Verify the exact file path or URL before upload and require explicit approval before using sensitive directories. <br>
Risk: Marketplace listings can set real USDC per-download pricing on Base mainnet. <br>
Mitigation: Confirm the listing intent, public visibility, and price before creating a paid listing. <br>
Risk: Payaion API credentials and marketplace scopes control upload, browse, and purchase capabilities. <br>
Mitigation: Use only the intended PAYAION_API_KEY, check authorization or scope errors, and avoid exposing the key in shared output. <br>


## Reference(s): <br>
- [Payaion](https://payaion.com) <br>
- [Payaion Dashboard](https://payaion.com/dashboard) <br>
- [Payaion Documentation](https://payaion.com/docs) <br>
- [Payaion OpenAPI Specification](https://payaion.com/openapi.yaml) <br>
- [Payaion Subscription and Pricing](https://payaion.com/docs/subscription) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown with curl commands and JSON response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses PAYAION_API_KEY and curl to call the Payaion REST API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
