## Description: <br>
Demio (demio.com). Use this skill for ANY Demio request - reading, creating, and updating data. Whenever a task involves Demio, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operations teams use this skill to operate Demio through an OOMOL-connected account, including listing events, inspecting event sessions and participants, and registering attendees after confirming write payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may query data from the connected Demio account. <br>
Mitigation: Use the connected account intentionally and review returned Demio data before sharing or acting on it. <br>
Risk: The register_attendee action changes Demio data and creates attendee access information. <br>
Mitigation: Confirm the exact registration payload and intended effect with the user before running the write action. <br>
Risk: Repeated setup or authentication commands could unnecessarily modify local CLI state or open account connection flows. <br>
Mitigation: Run one-time CLI, login, or connection setup only when a command fails with the matching setup or authentication error. <br>


## Reference(s): <br>
- [Demio homepage](https://www.demio.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-demio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects that include data and meta.executionId when actions are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
