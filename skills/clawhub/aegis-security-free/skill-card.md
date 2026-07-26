## Description: <br>
Aegis Security Free gives AI agents basic blockchain safety checks for address reputation, token honeypot detection, and free-tier usage monitoring on Ethereum and Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users can use this skill to guide read-only pre-transaction checks before sending funds or buying tokens. It helps query address reputation, token honeypot risk, and remaining free quota while keeping final crypto decisions subject to user review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The evidence notes inconsistent API key setup guidance. <br>
Mitigation: Clarify whether the free version needs an API key before installation, and store any required secret in a platform secret store rather than shell history or committed files. <br>
Risk: The skill uses a stable client fingerprint for quota tracking. <br>
Mitigation: Use a pseudonymous, non-sensitive identifier and avoid embedding personal data, wallet secrets, or private keys in the fingerprint value. <br>
Risk: Blockchain safety results may be incomplete or incorrect for financial decisions. <br>
Mitigation: Treat address and token checks as advisory, require user review for material transactions, and block or escalate HIGH and CRITICAL findings. <br>


## Reference(s): <br>
- [Aegis Security Free on ClawHub](https://clawhub.ai/thcjp/skills/aegis-security-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with curl commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only safety-check guidance; free version is limited to Ethereum and Base and results should be treated as advisory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
