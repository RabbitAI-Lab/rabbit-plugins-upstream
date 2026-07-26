## Description: <br>
Opsgenie helps agents read, create, acknowledge, close, fetch, and list Opsgenie alerts through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and incident responders use this skill to inspect Opsgenie action schemas, run valid connector payloads, and manage alert lifecycle tasks from an agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, acknowledge, or close Opsgenie alerts, which changes incident-management state. <br>
Mitigation: Require explicit user confirmation of the exact payload and expected effect before running write actions. <br>
Risk: The skill depends on an OOMOL-connected Opsgenie account with credentials available to the connector. <br>
Mitigation: Install only for intended Opsgenie use and keep the connected account scoped to the minimum Opsgenie permissions needed. <br>


## Reference(s): <br>
- [Opsgenie homepage](https://www.atlassian.com/software/opsgenie) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-opsgenie) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Opsgenie connector schemas before proposing or running write payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
