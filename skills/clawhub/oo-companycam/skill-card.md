## Description: <br>
Use this skill for CompanyCam requests, including reading, creating, updating, and deleting data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to operate a connected CompanyCam account through OOMOL, including reading company, user, project, and tag data and managing projects or tags when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, archive, restore, or delete CompanyCam data. <br>
Mitigation: Require explicit confirmation of the exact target and payload before running write or destructive actions. <br>
Risk: Authentication, connection scope, credential expiry, or billing errors can block CompanyCam actions. <br>
Mitigation: Use the documented setup or billing fallback only after a command fails with the matching error. <br>


## Reference(s): <br>
- [CompanyCam Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-companycam) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [CompanyCam Homepage](https://companycam.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Actions run through the OOMOL oo CLI and may return connector data with an execution id.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
