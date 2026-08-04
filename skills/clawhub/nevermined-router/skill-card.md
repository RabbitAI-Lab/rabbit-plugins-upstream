## Description: <br>
Guides an AI agent through using the Nevermined Router to discover x402 or MPP services, create a capped Delegation, fund the buyer wallet, make paid calls, read the payment ledger, and follow autonomous-spending guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nevermined-io](https://clawhub.ai/user/nevermined-io) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when an autonomous agent needs to pay per request for an external x402 or MPP service without holding a direct account or billing relationship with that service. It focuses on capped Delegations, Router calls, ledger review, and stop conditions for paid operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can spend real funds through x402 or MPP services when using live credentials and funded wallets. <br>
Mitigation: Use sandbox keys first, set small Delegation limits and short expiries, prefer recipient scoping when possible, and review the ledger for unexpected spending. <br>
Risk: Retrying paid calls with a new requestId can buy the same resource more than once. <br>
Mitigation: Use one stable requestId per logical purchase and reuse it across retries; only retry documented transient Router codes with backoff. <br>
Risk: Budget exhaustion, Delegation expiry, or an unfunded wallet can trigger stop-condition errors that should not be worked around by the agent. <br>
Mitigation: Treat BCK.ROUTER.0003 and BCK.ROUTER.0009 as human escalation points; do not widen a Delegation or create a replacement to bypass a refusal. <br>
Risk: The Nevermined API key could be exposed to paid merchants if forwarded as upstream authentication. <br>
Mitigation: Keep NVM_API_KEY private and use separate merchant credentials in forwarded headers when a merchant requires its own authentication. <br>
Risk: Catalog price labels are indicative and ledger amounts use atomic asset units rather than cents. <br>
Mitigation: Check settlement.approxCents on Router responses for the budget charge and reconcile ledger records against the agent's own requestId records. <br>


## Reference(s): <br>
- [Nevermined Router documentation](https://nevermined.ai/docs/products/router/overview) <br>
- [Nevermined app API keys](https://nevermined.app) <br>
- [Exa integration via Nevermined payments](https://nevermined.ai/docs/integrations/exa) <br>
- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md) <br>
- [Discovery - finding something to buy](references/discovery.md) <br>
- [Paying - mode B, streaming proxy, and mode A](references/paying.md) <br>
- [Errors and guardrails](references/errors.md) <br>
- [Ledger - what you actually spent](references/ledger.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with inline JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires NVM_API_KEY for authenticated Router, Delegation, and ledger calls; catalog discovery is public.] <br>

## Skill Version(s): <br>
0.1.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
