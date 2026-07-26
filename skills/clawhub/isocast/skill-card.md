## Description: <br>
Isocast is a Polymarket weather-signal API for AI agents that watches 37 cities and emits bucket-transition signals with market URLs, readings, live odds, optional Telegram delivery, free browse endpoints, and paid x402 signal bundles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Isocast to browse weather-linked Polymarket city data, inspect sample signal payloads, and retrieve paid per-city signal bundles when they have configured the required payment flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid endpoints can trigger x402 payment flows or use bearer receipts. <br>
Mitigation: Use free endpoints first, review service terms, and set spending limits before connecting a wallet, x402 payment client, or bearer receipt. <br>
Risk: The signal data is informational and betting-adjacent. <br>
Mitigation: Do not treat signals as financial or betting advice; confirm that use is appropriate for the user's jurisdiction and policy requirements. <br>
Risk: API calls can encounter payment, rate-limit, or unknown-city errors. <br>
Mitigation: Handle 402, 429, and 404 responses explicitly and respect Retry-After headers before retrying. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jcislo/skills/isocast) <br>
- [Isocast Homepage](https://isocast.dev) <br>
- [Isocast API Documentation](https://api.isocast.dev/llms.txt) <br>
- [Isocast OpenAPI Specification](https://api.isocast.dev/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, API calls, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript examples and JSON API response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node when using the MCP package; paid routes may require x402 payment setup.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
