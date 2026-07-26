## Description: <br>
ERC-8004 identity, x402 payments, and arbitration protocol for autonomous agent commerce. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lazaruseth](https://clawhub.ai/user/lazaruseth) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use Receipts Guard to manage autonomous-commerce agreements, DID-based identity, x402 payment terms, receipt capture, and arbitration workflows. It supports local CLI use and optional HTTP server deployment for cloud agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet and payment workflows can expose funds or private keys if deployed with a high-value wallet or poorly protected secrets. <br>
Mitigation: Use a dedicated low-balance wallet, store private keys only as protected secrets or environment variables, and avoid committing wallet material. <br>
Risk: Local receipt and identity storage may contain sensitive agreement, DID, key-history, and arbitration records. <br>
Mitigation: Protect the receipts directory, preserve restrictive private-key file permissions, and limit host access to trusted users. <br>
Risk: HTTP server mode exposes proposal, agreement, and listing workflows over the network. <br>
Mitigation: Configure RECEIPTS_API_KEY, keep CORS restricted to trusted origins, retain rate limiting, and test DID-signed authentication before relying on it. <br>
Risk: Recovery-controller verification can affect identity recovery decisions. <br>
Mitigation: Treat recovery-controller evidence as requiring manual review before accepting a recovery action. <br>


## Reference(s): <br>
- [Receipts Guard on ClawHub](https://clawhub.ai/lazaruseth/skills/receipts-guard) <br>
- [Publisher profile](https://clawhub.ai/user/lazaruseth) <br>
- [W3C DID Core](https://www.w3.org/ns/did/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with CLI commands, configuration snippets, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local receipt, identity, agreement, arbitration, ruling, export, and witness records when the commands are executed.] <br>

## Skill Version(s): <br>
0.7.1 (source: evidence.release.version, package.json, SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
