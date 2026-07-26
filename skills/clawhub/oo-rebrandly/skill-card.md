## Description: <br>
Rebrandly helps an agent operate a connected Rebrandly account to read, create, update, and soft-delete branded short links through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when they want an agent to manage Rebrandly account details, branded domains, and branded short links through their OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive actions can change or soft-delete Rebrandly links. <br>
Mitigation: Confirm the exact payload, target, and expected effect with the user before creating, updating, or deleting links. <br>
Risk: Fallback first-time setup may run an oo CLI install script. <br>
Mitigation: Review the oo CLI install script before running fallback setup commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rebrandly) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Rebrandly homepage](https://www.rebrandly.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector action results are returned as JSON with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
