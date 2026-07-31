## Description: <br>
Digistore24 helps agents retrieve Digistore24 account data through an OOMOL-connected account and the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to retrieve buyers, products, purchases, sales, and account-owner information from a connected Digistore24 account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Digistore24 account data such as buyers, purchases, products, and user information through the connected OOMOL account. <br>
Mitigation: Install and use it only when that account-data access is acceptable for the workspace and user. <br>
Risk: Using an incorrect or outdated payload could query the wrong Digistore24 record or fail unexpectedly. <br>
Mitigation: Review the live action schema before constructing each payload. <br>
Risk: First-time setup commands can start installation, sign-in, or account-connection flows. <br>
Mitigation: Run setup steps only after the matching CLI, authentication, or connection error occurs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-digistore24) <br>
- [Digistore24 Homepage](https://www.digistore24.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
