## Description: <br>
Enable AI agents to make micropayments via x402 protocol. Use when purchasing browser sessions on Browserbase, scraping with Firecrawl, or any x402-compatible API. Handles wallet creation, funding, and automatic payment flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emilankerwiik](https://clawhub.ai/user/emilankerwiik) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to discover x402-compatible services, create or manage a thirdweb server wallet, fund and check balances, and make paid API requests through x402 payment flows. It is intended for workflows that need browser automation sessions, scraping services, disposable inboxes, or other APIs that require micropayments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate payment-capable API requests and manage wallet funding flows. <br>
Mitigation: Use a dedicated low-balance wallet, set per-request payment limits such as maxValue, and review each paid request before execution. <br>
Risk: The thirdweb secret key grants access to wallet and payment operations. <br>
Mitigation: Use a least-privileged thirdweb key for this skill, store it only in the environment, and rotate it if exposed. <br>
Risk: Disposable inbox credentials and mailbox tokens may be written to .agent-emails.json. <br>
Mitigation: Treat .agent-emails.json as sensitive, keep it out of version control, and delete stored inboxes and tokens when no longer needed. <br>
Risk: Some x402-like services may be non-standard or incompatible with automated payment handling. <br>
Mitigation: Prefer services that return standard 402 payment details and test with small requests before relying on a service. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/emilankerwiik/skills/openkrill) <br>
- [x402 API Reference](references/API-REFERENCE.md) <br>
- [x402-Compatible Services](references/SERVICES.md) <br>
- [x402 Protocol](https://x402.org) <br>
- [x402 Bazaar Discovery](https://docs.cdp.coinbase.com/x402/bazaar) <br>
- [thirdweb x402 Documentation](https://portal.thirdweb.com/x402) <br>
- [Browserbase x402 Docs](https://docs.browserbase.com/integrations/x402/introduction) <br>
- [Firecrawl x402 Docs](https://docs.firecrawl.dev/x402/search) <br>
- [Mail.tm Documentation](https://docs.mail.tm) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, TypeScript helper scripts, JSON configuration, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, THIRDWEB_SECRET_KEY, and funded wallet credentials for paid x402 requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
