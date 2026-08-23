## Description:

Helps agents discover, compare, buy, and retrieve Freeland prepaid travel eSIMs through x402 with native USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elvismusli](https://clawhub.ai/user/elvismusli)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to find travel eSIM plans, confirm live pricing, complete an x402 USDC payment on Base, and privately retrieve activation credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through a real USDC-on-Base eSIM purchase.

Mitigation: Proceed only when the user intends to buy or retrieve a Freeland eSIM, and show the selected plan, destination coverage, allowance, duration, and exact USDC amount before any wallet signature.

Risk: A changed live plan price or payment requirement could make a quote stale.

Mitigation: Treat live plan data and payment requirements as authoritative, stop on changed price or requirement, and request a fresh user authorization before payment.

Risk: Delivery tokens, QR codes, LPA activation data, ICCIDs, and installation links can expose the purchased eSIM.

Mitigation: Keep delivery tokens and activation credentials private, avoid public logs or shared artifacts, and deliver credentials only through a private, non-cacheable channel to the capability holder or authenticated owner.

Risk: A lost paid response or unclear timeout could lead to a mistaken repeat purchase.

Mitigation: Reuse the original idempotency key and purchase body for recovery, require a replayed settled order when recovering, and do not create a replacement order without a new explicit owner decision.

Risk: Wallet authority or private keys could be exposed if delegated to the wrong tool.

Mitigation: Use the remote MCP only for read-only discovery and never request, expose, or delegate seed phrases or private keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elvismusli/skills/freeland-x402-esim)
- [Freeland eSIM discovery contract](https://api.x402card.org/api/esim/discovery)
- [x402card read-only MCP endpoint](https://api.x402card.org/mcp)
- [Freeland eSIM readiness endpoint](https://api.x402card.org/api/esim/ready)
- [Freeland eSIM purchase endpoint](https://api.x402card.org/api/esim/purchase)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or private text with live plan details, payment guidance, order status, and eSIM activation credentials.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive order IDs, delivery tokens, QR codes, LPA activation data, ICCID, and installation links that must remain private.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
