## Description: <br>
Elfa AI helps agents use the Elfa API for crypto social intelligence, market context, automated condition monitoring, integration examples, and optional live trading workflows through Auto and Trade endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nero-sensei](https://clawhub.ai/user/nero-sensei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent builders use this skill to query Elfa crypto intelligence, generate API integration snippets, and configure automated market alerts or trading workflows against Elfa API endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable live financial actions, including exchange linking, order placement, cancellation, deletion, recurring automation, and trade execution. <br>
Mitigation: Use accounts and API keys suitable for agent access, prefer read-only or test credentials where possible, and require explicit human confirmation before any live trade, exchange-linking, cancellation, deletion, or recurring automation action. <br>
Risk: Credential-bearing workflows involve API keys, HMAC secrets, x402 agent secrets, payment signatures, and wallet-related setup. <br>
Mitigation: Load credentials from environment variables or local secret stores, avoid pasting secrets into chat, avoid printing environment variables, and keep wallet private keys client-side. <br>
Risk: Market automation can misfire, over-trigger, or act on stale assumptions when endpoint behavior, supported assets, prices, or trading rules change. <br>
Mitigation: Validate and preview queries or orders before activation, use conservative cooldowns and trigger caps, monitor active automations, and verify current endpoint behavior against Elfa documentation before acting. <br>


## Reference(s): <br>
- [Elfa documentation](https://docs.elfa.ai) <br>
- [Elfa API](https://api.elfa.ai) <br>
- [Elfa Auto documentation](https://docs.elfa.ai/auto/overview) <br>
- [Elfa Trade documentation](https://docs.elfa.ai/trade/overview) <br>
- [Elfa x402 payments documentation](https://docs.elfa.ai/x402-payments) <br>
- [OpenAPI reference](artifact/references/swagger.json) <br>
- [ClawHub skill page](https://clawhub.ai/nero-sensei/skills/elfa-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, curl, Python, and JavaScript/TypeScript examples; live API responses may be JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require ELFA_API_KEY, ELFA_HMAC_SECRET, ELFA_AGENT_SECRET, curl, and optionally jq or python3.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
