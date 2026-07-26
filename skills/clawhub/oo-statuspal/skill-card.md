## Description: <br>
StatusPal routes StatusPal requests through the OOMOL oo CLI connector for searching and reading status page, incident, and service data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to query StatusPal status pages, incidents, and services from an OOMOL-connected account through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad or vague StatusPal requests could cause the agent to query account, status page, incident, or service data the user did not intend to inspect. <br>
Mitigation: Confirm the intended StatusPal page, incident, service, or query before running connector reads when the request is ambiguous. <br>
Risk: The skill depends on the oo CLI and a connected StatusPal account, so setup, credential, scope, or billing failures can interrupt use. <br>
Mitigation: Use the documented setup and recovery steps only after a matching command failure, and do not initiate sign-in or connection flows proactively. <br>


## Reference(s): <br>
- [StatusPal homepage](https://www.statuspal.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [StatusPal skill on ClawHub](https://clawhub.ai/oomol/skills/oo-statuspal) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON payload examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON with data and metadata fields when actions run successfully.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
