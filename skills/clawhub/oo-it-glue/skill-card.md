## Description: <br>
This skill helps agents search and retrieve IT Glue organizations, users, contacts, and configurations through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill when an agent needs to search or read IT Glue records for organizations, users, contacts, and configurations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can retrieve IT Glue records through an OOMOL-connected account when invoked. <br>
Mitigation: Use the skill only for explicit IT Glue read requests, and inspect the action schema before sending payloads. <br>
Risk: Use depends on trusting OOMOL, the oo CLI, and the connected IT Glue account. <br>
Mitigation: Install and connect the oo CLI only in environments where OOMOL and the account connection are approved. <br>


## Reference(s): <br>
- [IT Glue homepage](https://www.itglue.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-it-glue) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only IT Glue get and list actions; inspect the live action schema before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
