## Description: <br>
Daffy (daffy.org) connector for searching and reading Daffy account, user, nonprofit, donation, and contribution data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect Daffy account information, look up nonprofits and users, and list donation or contribution records through the Daffy connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Daffy account information, including balance, contributions, and donations, through the user's OOMOL connection. <br>
Mitigation: Install and use it only when that account-level access is acceptable, and limit outputs to the information needed for the user's request. <br>
Risk: Future write-capable Daffy actions could change account state if added to the connector. <br>
Mitigation: Require explicit user confirmation of the exact action, payload, and expected effect before running any action tagged write or destructive. <br>
Risk: The first-time setup path depends on a trusted oo CLI installation and an active Daffy connection. <br>
Mitigation: Treat CLI installation and account connection as trusted setup steps, and run setup only after an authentication or connection failure. <br>


## Reference(s): <br>
- [ClawHub Daffy skill page](https://clawhub.ai/oomol/skills/oo-daffy) <br>
- [Daffy homepage](https://www.daffy.org/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Daffy connector actions unless future actions are explicitly tagged as write or destructive.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
