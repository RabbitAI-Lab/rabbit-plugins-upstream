## Description: <br>
Operate Drata through an OOMOL-connected account to search and read company metadata, controls, personnel, vendors, and workspaces using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and developers responsible for compliance operations use this skill to read Drata company, control, personnel, vendor, and workspace data through their connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read sensitive Drata company, personnel, vendor, control, and workspace records visible to the connected OOMOL account. <br>
Mitigation: Install and use the skill only for intended Drata access, review Drata connection scopes, and prefer the least-privileged account that can complete the task. <br>
Risk: Running setup or connection steps unnecessarily could change the user's local CLI session or OOMOL connection state. <br>
Mitigation: Run setup, login, or connection steps only after an oo CLI, authentication, or Drata connection error requires them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-drata) <br>
- [Drata Homepage](https://drata.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Drata data is returned through oo connector responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
