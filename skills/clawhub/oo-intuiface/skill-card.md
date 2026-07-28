## Description: <br>
Operate Intuiface through an OOMOL-connected account to list running experiences and send confirmed Web Trigger messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and external users use this skill to operate Intuiface through OOMOL, inspect live connector schemas, list running experiences, and send approved Web Trigger messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The send_message action can trigger behavior in running Intuiface experiences. <br>
Mitigation: Review and approve the exact send_message payload and expected effect before running the write action. <br>
Risk: Using the skill requires an OOMOL-connected Intuiface account and may require oo CLI setup or API-key connection through OOMOL. <br>
Mitigation: Install the skill only when agents should use that connected account, and perform setup only after an auth or connection failure indicates it is needed. <br>


## Reference(s): <br>
- [ClawHub Intuiface skill page](https://clawhub.ai/oomol/skills/oo-intuiface) <br>
- [Intuiface homepage](https://www.intuiface.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before action execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
