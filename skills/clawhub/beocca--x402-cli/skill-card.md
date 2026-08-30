## Description:

A simple CLI that helps AI agents discover x402 services and make paywalled requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beocca](https://clawhub.ai/user/beocca)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use x402-CLI to discover x402-enabled services, inspect their payment requirements, and make paywalled HTTP requests from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend real Base USDC from the configured wallet without a built-in approval step.

Mitigation: Use a fresh, dedicated wallet with a very small balance and add an external approval gate before allowing an agent to call request pay.

Risk: Agents can send payments or request data from arbitrary x402 service URLs, including untrusted or malicious endpoints.

Mitigation: Use domain and recipient allowlists, inspect payment requirements with request info first, and monitor paid requests.

Risk: The wallet private key is supplied through CLIENT_EVM_WALLET_SECRET and exposure gives control of the wallet.

Mitigation: Do not use a personal or high-value wallet, avoid hardcoding or logging the secret, and clear the environment variable after use.

Risk: Saved request and response files may contain sensitive request bodies or service responses.

Mitigation: Avoid --save when interacting with untrusted services or when request bodies and responses may contain secrets or sensitive data.

## Reference(s):

- [x402-CLI ClawHub Skill Page](https://clawhub.ai/beocca/skills/x402-cli)
- [x402 Official Site](https://x402.org/)
- [x402 Documentation](https://docs.x402.org/introduction)
- [x402 GitHub Repository](https://github.com/x402-foundation/x402)
- [CDP x402 Facilitator Docs](https://docs.cdp.coinbase.com/x402/introduction)
- [x402scan](https://www.x402scan.com/)
- [x402scan GitHub Repository](https://github.com/Merit-Systems/x402scan)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON responses on stdout, optional saved JSON files, and Markdown usage guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return one JSON object with stable error_code values; request pay requires CLIENT_EVM_WALLET_SECRET and can move Base USDC.]

## Skill Version(s):

1.2.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
