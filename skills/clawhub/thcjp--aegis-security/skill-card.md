## Description: <br>
Aegis Security guides agents through blockchain safety checks for wallet addresses, token contracts, transaction simulations, quota usage, and x402-paid API requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, security analysts, and external agent users can use this skill to plan blockchain risk checks before transfers, DeFi interactions, or token purchases. It is intended for address reputation checks, token honeypot screening, transaction simulation guidance, and quota or payment handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review verdict is suspicious because the skill requests broad read and execution authority while guiding blockchain API use. <br>
Mitigation: Review before installing and grant only the minimum local file or command access needed for explicit address, token, transaction simulation, or quota checks. <br>
Risk: The skill includes x402 paid request flows and wallet-signer guidance. <br>
Mitigation: Require explicit user confirmation before any paid request or wallet-signer use, and never provide private keys, seed phrases, or raw signing secrets. <br>
Risk: Quota and tracking behavior depends on a client fingerprint, and unstable or overly identifying fingerprints can create privacy or billing ambiguity. <br>
Mitigation: Use a stable pseudonymous fingerprint only, monitor quota usage, and avoid rotating fingerprints to bypass limits. <br>
Risk: Blockchain risk checks and transaction simulations can be incomplete or wrong for critical asset decisions. <br>
Mitigation: Treat LOW, MEDIUM, HIGH, and CRITICAL outputs as decision support, require human review for significant transfers, and block or escalate high-risk results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aegis-security) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with curl examples and JSON API response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces safety decision guidance, risk levels, threat signals, quota status, and payment-handling instructions; results are not a 100% security guarantee.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
