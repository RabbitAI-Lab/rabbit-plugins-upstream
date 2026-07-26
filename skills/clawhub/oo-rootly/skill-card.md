## Description: <br>
Rootly (rootly.com). Use this skill for ANY Rootly request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and incident-response operators use this skill to search and read Rootly users, incidents, services, and teams through an OOMOL-connected Rootly account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rootly incident and account data may be sensitive. <br>
Mitigation: Use the skill only for explicit Rootly tasks and treat returned incident, user, service, and team data as sensitive. <br>
Risk: Live connector schemas may differ from assumed payload shapes. <br>
Mitigation: Inspect the action schema with the oo CLI before constructing payloads. <br>
Risk: Authentication, connection, scope, credential, or billing errors can block Rootly access. <br>
Mitigation: Use the documented setup and recovery steps only after a command fails for the matching reason. <br>


## Reference(s): <br>
- [ClawHub Rootly skill page](https://clawhub.ai/oomol/skills/oo-rootly) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Rootly homepage](https://rootly.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Rootly connector responses are returned by the oo CLI as JSON when commands are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release version and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
