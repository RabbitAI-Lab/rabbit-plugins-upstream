## Description:

Guides an agent through buying x402 or MPP service calls with the Nevermined Router, including service discovery, capped Delegation setup, wallet funding, routed or streaming calls, ledger review, and spend guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when an autonomous agent needs to buy a single call from an external x402 or MPP service without a direct account or billing relationship, while keeping spend within a human-capped Delegation and reconciling payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can initiate paid Nevermined Router service calls.

Mitigation: Use sandbox first, create small capped Delegations with short expiries, scope recipients where possible, and require human review before increasing budgets or funding wallets.

Risk: The NVM_API_KEY authorizes the agent to Nevermined and could be exposed if forwarded to merchants.

Mitigation: Keep NVM_API_KEY out of merchant headers and only pass merchant-specific authentication through routed request headers when needed.

Risk: Failed spend limits, legal consent requirements, or wallet funding gaps can tempt automated retries or budget changes.

Mitigation: Treat those conditions as stop points for human review rather than automatically widening Delegations, creating replacement Delegations, accepting legal terms, or retrying non-retryable payment errors.

## Reference(s):

- [ClawHub nevermined-router release page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router product documentation](https://nevermined.ai/docs/products/router/overview)
- [Nevermined app API keys](https://nevermined.app)
- [Nevermined Exa integration](https://nevermined.ai/docs/integrations/exa)
- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Errors and guardrails](references/errors.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Paying - mode B, the streaming proxy, and mode A](references/paying.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY and human-managed spend caps; the skill guides agent behavior rather than producing persistent files.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
