## Description: <br>
Workspace Anchor helps agents discover, list, create, switch, and validate project anchors based on `.project-lock` files so work stays oriented to the intended workspace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenchantlive](https://clawhub.ai/user/zenchantlive) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to manage multi-agent project context, locate workspace anchors, create `.project-lock` files, and check whether paths belong to the active project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad filesystem discovery can scan more of a user's machine than intended. <br>
Mitigation: Configure explicit, narrow workspace roots and avoid discovery across the full home directory. <br>
Risk: Unsafe shell command construction can expose users to command execution risks when paths or inputs are not tightly controlled. <br>
Mitigation: Review the skill before installation and use only trusted paths and project names until command construction is fixed. <br>
Risk: Path validation should not be treated as a security boundary. <br>
Mitigation: Use the validation output as workflow guidance and keep independent access controls, reviews, and scans in place. <br>


## Reference(s): <br>
- [Workspace Anchor on ClawHub](https://clawhub.ai/zenchantlive/skills/workspace-anchor) <br>
- [Publisher profile](https://clawhub.ai/user/zenchantlive) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and structured JSON/text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workspace discovery, listing, switching, creation, status, and path-validation guidance for agent workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
