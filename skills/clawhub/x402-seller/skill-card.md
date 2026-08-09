## Description: <br>
Autonomously monetize your services with x402 payment collection. Set up an x402 server, define paid endpoints, and accept programmatic payments in stablecoins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to design, deploy, and operate x402-protected HTTP services that collect stablecoin payments for API access or other programmatic work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Production or mainnet configuration can handle live payments and expose financial loss if credentials, prices, routes, or settlement behavior are wrong. <br>
Mitigation: Use testnet first, keep CDP credentials and wallet secrets out of code, use scoped production secrets, confirm prices and protected routes, and monitor settlement and costs after launch. <br>


## Reference(s): <br>
- [x402 Technical Reference](artifact/x402DOCS.md) <br>
- [Service Ideation Guide](artifact/IDEATION.md) <br>
- [Minimal FastAPI Seller Example](artifact/example/README.md) <br>
- [x402 Official Site](https://x402.org/) <br>
- [x402 Documentation](https://docs.x402.org/introduction) <br>
- [CDP Getting Started](https://docs.cdp.coinbase.com/get-started/overview) <br>
- [CDP x402 Facilitator Docs](https://docs.cdp.coinbase.com/x402/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and runnable Python example code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes guidance for wallet setup, facilitator configuration, endpoint pricing, deployment options, and payment verification practices.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
