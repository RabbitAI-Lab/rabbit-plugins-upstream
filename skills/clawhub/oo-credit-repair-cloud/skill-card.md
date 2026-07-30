## Description: <br>
Operates Credit Repair Cloud through an OOMOL connector for reading, creating, updating, and deleting supported records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Credit Repair Cloud through an OOMOL-connected account, including viewing, creating, updating, and deleting lead/client and affiliate records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform write and destructive actions against a user's OOMOL-connected Credit Repair Cloud account. <br>
Mitigation: Review exact write and delete payloads before approval, and require explicit confirmation for destructive targets. <br>
Risk: First-time setup may require installing or logging in to the oo CLI. <br>
Mitigation: Run installer or login flows only when needed, and only when the user trusts OOMOL and intends to connect Credit Repair Cloud. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-credit-repair-cloud) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Credit Repair Cloud Homepage](https://www.creditrepaircloud.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
