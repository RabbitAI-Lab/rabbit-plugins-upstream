## Description: <br>
Operate Livespace CRM through an OOMOL-connected account for reading, creating, updating, and deleting CRM data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External teams and CRM operators use this skill to let an agent retrieve and maintain Livespace companies, deals, people, users, and todos through the OOMOL CLI. It supports read workflows directly and state-changing workflows after the user confirms the exact requested effect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approved write actions can create or modify real Livespace CRM records. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Approved destructive actions can remove Livespace companies, deals, people, or todos. <br>
Mitigation: Confirm the target record and get explicit approval before running delete actions. <br>


## Reference(s): <br>
- [ClawHub Livespace skill](https://clawhub.ai/oomol/skills/oo-livespace) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Livespace](https://www.livespace.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
