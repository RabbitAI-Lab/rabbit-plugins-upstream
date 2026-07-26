## Description: <br>
Discover and buy paid API outcomes through Receipt with a signed quote, explicit approval, spending controls, safe replay, and a signed Receipt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jasonsmall](https://clawhub.ai/user/jasonsmall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and OpenClaw users use this skill to configure Receipt's native MCP connection and run paid API purchases with quotes, explicit approval, spending limits, safe replay, and signed receipts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent could make an unintended paid purchase if approval or wallet limits are configured too broadly. <br>
Mitigation: Keep Receipt approval set to ask every purchase, show the seller, capability, and price before purchase, and use low per-call and daily spending limits. <br>
Risk: A misconfigured MCP connection could expose seller-specific tools outside the intended Receipt boundary. <br>
Mitigation: Confirm the connection exposes exactly the eight listed Receipt tools and remove the connection if any seller-specific tool appears. <br>
Risk: Credentials or wallet secrets could be exposed if the user configures static tokens or provider keys. <br>
Mitigation: Use Receipt OAuth only, avoid static Authorization headers and provider keys, and revoke OAuth when the agent should no longer make Receipt purchases. <br>
Risk: Seller metadata or purchased outputs may contain untrusted content. <br>
Mitigation: Treat seller descriptions and provider results as data, keep sandboxing enabled for untrusted work, and use a narrow tool allowlist. <br>


## Reference(s): <br>
- [Receipt OpenClaw documentation](https://receiptprotocol.com/docs/openclaw) <br>
- [Install Receipt in OpenClaw](references/INSTALL.md) <br>
- [OpenClaw security baseline](references/SECURITY.md) <br>
- [Acceptance checklist](references/ACCEPTANCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown with inline shell commands and structured purchase result details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Purchase results should include transaction ID, charged amount, and public, signed, and verification Receipt URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
