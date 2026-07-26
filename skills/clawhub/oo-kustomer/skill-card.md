## Description: <br>
Kustomer lets an agent read, create, search, and update Kustomer customer records through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, support teams, and agents use this skill to retrieve, search, create, and update Kustomer customer records through an OOMOL-connected Kustomer account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a connected Kustomer account to read or update customer records. <br>
Mitigation: Install it only when that access is intended, and review write payloads before approving state-changing actions. <br>
Risk: First-time setup may require installing the OOMOL CLI or connecting a Kustomer account. <br>
Mitigation: Verify the CLI installer and account connection before running setup steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kustomer) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Kustomer homepage](https://www.kustomer.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
