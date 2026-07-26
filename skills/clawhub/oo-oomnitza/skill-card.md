## Description: <br>
Oomnitza (oomnitza.com). Use this skill for Oomnitza requests that search and read data through the OOMOL connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and developers use this skill to validate an Oomnitza connection and retrieve Oomnitza asset or user information through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on an installed and authenticated oo CLI plus an active Oomnitza connection. <br>
Mitigation: Use the documented first-time setup path only after a command fails with an installation, authentication, connection, or billing error. <br>
Risk: Future connector actions could include write or destructive operations even though this release is read-only. <br>
Mitigation: Limit use to the listed read-only actions and require explicit user confirmation before any future action tagged write or destructive is run. <br>


## Reference(s): <br>
- [Oomnitza homepage](https://www.oomnitza.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oomnitza) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo CLI connector schema and run commands; connector responses are JSON with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
