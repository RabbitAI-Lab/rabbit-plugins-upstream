## Description: <br>
Uploadcare (uploadcare.com). Use this skill for ANY Uploadcare request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to operate Uploadcare through an OOMOL-connected account for file, group, and project reads, plus approved file storage and deletion actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Uploadcare state, including permanently storing files and deleting files by UUID. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before write or destructive actions. <br>
Risk: The connected Uploadcare account may expose project, file, and group data through OOMOL's oo CLI. <br>
Mitigation: Connect only an Uploadcare account whose access level is appropriate for agent operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-uploadcare) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Uploadcare homepage](https://uploadcare.com) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, text] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Actions return JSON data with execution metadata when run through the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
