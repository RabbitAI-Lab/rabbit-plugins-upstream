## Description: <br>
OrcaTrace gives agents Polymarket intelligence through documented free and paid API endpoints for real-time market repricings, whale-calibration signals, intelligence digests, resolving markets, and on-demand single-market research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and AI-agent builders use OrcaTrace to add Polymarket intelligence, market-monitoring, and informational research workflows to agents through free and pay-per-call API endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries to an external Polymarket-intelligence API and automated paid calls may disclose usage patterns or incur USDC charges. <br>
Mitigation: Review endpoint prices and payment requirements first, use free sample and proof endpoints for shape testing, and limit automated paid calls. <br>
Risk: Paid routes require wallet signing and private-key handling for x402 payments on Base. <br>
Mitigation: Use secure key management, prefer a constrained wallet for automation, and keep private keys out of prompts, logs, and shared files. <br>
Risk: Public-chain wallet analytics and model-generated prediction-market analysis can carry privacy, accuracy, and financial-decision risks. <br>
Mitigation: Treat results as informational, verify claims against public market and chain data, and avoid relying on the output as financial advice. <br>


## Reference(s): <br>
- [ClawHub OrcaTrace release](https://clawhub.ai/jcislo/skills/orcatrace) <br>
- [OrcaTrace homepage](https://orcatrace.dev) <br>
- [OrcaTrace API](https://api.orcatrace.dev) <br>
- [Free track-record endpoint](https://api.orcatrace.dev/v1/track-record) <br>
- [OpenAPI schema](https://api.orcatrace.dev/openapi.json) <br>
- [x402 payment manifest](https://api.orcatrace.dev/.well-known/x402) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API calls, Configuration] <br>
**Output Format:** [Markdown with endpoint tables, curl commands, and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node for the x402 client examples; paid calls use USDC on Base.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
