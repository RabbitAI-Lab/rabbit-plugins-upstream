## Description: <br>
TextIt lets an agent use OOMOL's oo CLI connector to read, create, update, delete, and send data in a connected TextIt workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage TextIt workspaces from an agent through the OOMOL oo connector, including listing workspace data, managing contacts and groups, and sending messages or broadcasts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change contacts, groups, messages, or broadcasts in the connected TextIt workspace. <br>
Mitigation: Confirm the exact payload, recipients, and expected effect with the user before running write actions. <br>
Risk: Destructive actions can delete TextIt contacts or groups. <br>
Mitigation: Require explicit approval for the target UUID or URN before running destructive actions. <br>


## Reference(s): <br>
- [TextIt skill page](https://clawhub.ai/oomol/skills/oo-textit) <br>
- [TextIt homepage](https://textit.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo connector schema and run commands; write and destructive actions should include explicit recipient, payload, and target confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
