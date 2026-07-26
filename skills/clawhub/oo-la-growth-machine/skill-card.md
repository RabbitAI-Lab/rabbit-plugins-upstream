## Description: <br>
Enables agents to operate La Growth Machine through OOMOL's la_growth_machine connector for reading, creating, and updating audiences and leads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers with an OOMOL-connected La Growth Machine account use this skill to inspect schemas, run account and lead queries, and perform confirmed audience or lead changes through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change La Growth Machine CRM lead and audience data. <br>
Mitigation: Review the exact create or update payload with the user and get confirmation before running write actions. <br>
Risk: First-time CLI installation introduces an additional trust decision when oo is not already installed. <br>
Mitigation: Treat installation separately from connector use and proceed only when the user intentionally uses OOMOL for the connected La Growth Machine account. <br>
Risk: Authentication, missing scopes, expired credentials, billing stops, or disconnected app state can block connector execution. <br>
Mitigation: Use the documented first-time setup and troubleshooting steps only after a command fails with the matching error. <br>


## Reference(s): <br>
- [La Growth Machine homepage](https://lagrowthmachine.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-la-growth-machine) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
