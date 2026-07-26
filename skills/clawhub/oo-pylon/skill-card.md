## Description: <br>
Pylon lets an agent read, create, and update Pylon records through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Pylon support and customer records from an agent session, including issue, account, contact, and organization workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update live Pylon records through a connected OOMOL account. <br>
Mitigation: Confirm write payloads and expected effects with the user before running write actions. <br>
Risk: First-time setup may install or authenticate the oo CLI if the tool is missing or disconnected. <br>
Mitigation: Use setup fallbacks only after a matching command failure and only when the user trusts the OOMOL CLI process. <br>


## Reference(s): <br>
- [Pylon homepage](https://www.usepylon.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
