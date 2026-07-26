## Description: <br>
Checks blockchain addresses and token contracts for reputation, honeypot, and basic risk signals before DeFi transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run lightweight blockchain address and token safety checks before trades, transfers, or small-scale DeFi reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends queried blockchain addresses, token contracts, chain IDs, and any client fingerprint header to aegis402.xyz. <br>
Mitigation: Use the skill only for intended blockchain checks, avoid personal or host-derived fingerprints, and use a random opaque identifier if quota tracking is needed. <br>
Risk: The security scan verdict is suspicious because the skill asks for broad command execution and includes third-party network calls. <br>
Mitigation: Review commands before execution, restrict use to trusted environments, and confirm that requests only target the expected Aegis endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/aegis-security-tool-free) <br>
- [Aegis service health endpoint](https://aegis402.xyz/health) <br>
- [Aegis usage endpoint](https://aegis402.xyz/v1/usage) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces risk-level guidance from third-party blockchain address and token checks; free tier usage is limited.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
