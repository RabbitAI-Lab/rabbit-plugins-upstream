## Description: <br>
Operate DeskTime through an OOMOL-connected account for reading, creating, and updating DeskTime data instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and operations teams use this skill to operate DeskTime through an OOMOL-connected account. It supports reading company, employee, project, task, and tracking information, and creating DeskTime projects with optional tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger wording could cause DeskTime actions to run when the user's intent is unclear. <br>
Mitigation: Require clear user intent before allowing DeskTime actions, especially operations that create or change records. <br>
Risk: DeskTime write actions can create or change records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write or destructive. <br>
Risk: The integration requires DeskTime-related credentials and account access through OOMOL. <br>
Mitigation: Before installation, confirm the user is comfortable granting the DeskTime access needed for the integration. <br>


## Reference(s): <br>
- [ClawHub DeskTime Skill](https://clawhub.ai/oomol/skills/oo-desktime) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [DeskTime Homepage](https://desktime.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing DeskTime action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
