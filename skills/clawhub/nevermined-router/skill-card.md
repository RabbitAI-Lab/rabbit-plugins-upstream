## Description:

Helps an AI agent pay external x402 or MPP services through the Nevermined Router, including service discovery, capped Delegation setup, routed paid calls, ledger review, and autonomous-buyer guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous-agent operators use this skill when an agent needs to buy single calls from external x402 or MPP services without holding the merchant's account credentials. It guides the agent through finding payable services, creating and funding a capped Delegation, making paid Router calls, and auditing spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent is asked to hold a Nevermined account-owner API key that can create new spending Delegations beyond a single preapproved budget.

Mitigation: Prefer sandbox first, create the smallest practical Delegation, set allowedRecipients and maxTransactions when possible, monitor the ledger, and avoid unattended live-fund use unless the user accepts that spend risk.

Risk: A fresh requestId on retries, widening a Delegation, or creating a replacement Delegation after a refusal can cause duplicate purchases or spend beyond the user's intended cap.

Mitigation: Use one stable requestId per logical purchase, stop on budget or wallet refusals, and require a human decision before increasing or replacing a Delegation.

Risk: A catalog service may be routable in general but not payable from the selected deployment, rail, network, or allowlist configuration.

Mitigation: Filter for x402 or MPP services, preflight the Delegation and funded network, prefer the documented Router route flow, and treat non-retryable Router refusals as stop conditions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nevermined-io/skills/nevermined-router)
- [Nevermined Router documentation](https://nevermined.ai/docs/products/catalog/router/overview)
- [Nevermined app](https://nevermined.app)
- [Bootstrap - API key, Delegation, funded wallet](references/bootstrap.md)
- [Discovery - finding something to buy](references/discovery.md)
- [Paying - mode B, streaming proxy, and mode A](references/paying.md)
- [Ledger - what you actually spent](references/ledger.md)
- [Errors and guardrails](references/errors.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl/bash examples and JSON request and response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NVM_API_KEY and human-approved spending limits before live paid calls.]

## Skill Version(s):

0.1.12 (source: server release metadata; artifact frontmatter states 0.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
