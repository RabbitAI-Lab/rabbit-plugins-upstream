## Description: <br>
GageList (gagelist.com). Use this skill for GageList requests such as reading, creating, updating, and deleting account data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected GageList account through OOMOL, including account status checks, gage and calibration record lookups, and manufacturer management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify connected GageList account data through write actions. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: The delete_manufacturer action can remove manufacturer records. <br>
Mitigation: Require explicit user approval of the target record before running destructive actions. <br>
Risk: First-time setup may install the oo CLI and require connecting GageList credentials in OOMOL. <br>
Mitigation: Proceed with setup only when the user intends to grant account access and understands the credential connection requirement. <br>


## Reference(s): <br>
- [GageList homepage](https://gagelist.com/) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gagelist) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return JSON responses from OOMOL connector actions when commands are executed.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
