## Description: <br>
Lumos helps agents read and search Lumos access requests and AppStore app records through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to retrieve Lumos access-request and AppStore-app data from a connected Lumos account without handling raw credentials directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may construct an invalid or stale Lumos connector payload. <br>
Mitigation: Fetch the live connector schema with `oo connector schema` before constructing each action payload. <br>
Risk: A state-changing Lumos action could affect the wrong target if write or destructive actions are later added. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged `[write]` or `[destructive]`. <br>
Risk: Authentication or connection setup may be attempted unnecessarily. <br>
Mitigation: Run first-time setup commands only after the matching command-not-found, authentication, connection, scope, or billing error appears. <br>


## Reference(s): <br>
- [ClawHub Lumos skill](https://clawhub.ai/oomol/skills/oo-lumos) <br>
- [Lumos homepage](https://www.lumos.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live Lumos connector schemas before execution; read actions are safe to run directly, while write or destructive actions require confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
