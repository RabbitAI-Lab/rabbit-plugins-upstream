## Description: <br>
Smartsheet lets agents read, create, update, and delete Smartsheet data through an OOMOL-connected account instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate sheets available to an OOMOL-connected Smartsheet account, including listing sheets, retrieving sheet data, and adding, updating, or deleting rows after confirming write or destructive payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access Smartsheet data available to the connected OOMOL account. <br>
Mitigation: Install and use it only when that account's Smartsheet access is appropriate for the task. <br>
Risk: Add, update, and delete actions can change or remove sheet data. <br>
Mitigation: Review the exact payload and expected effect, and get explicit approval before write or destructive actions. <br>
Risk: First-time setup or login steps can change authentication or connection state. <br>
Mitigation: Run install, login, or connection steps only when a command fails for the matching setup reason. <br>


## Reference(s): <br>
- [ClawHub Smartsheet Skill Page](https://clawhub.ai/oomol/skills/oo-smartsheet) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Smartsheet](https://www.smartsheet.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline oo CLI commands and JSON payloads or responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Smartsheet row and column data, execution metadata, and proposed write or delete payloads for review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
