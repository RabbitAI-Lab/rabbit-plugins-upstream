## Description: <br>
Clean up node_modules and .next folders to free up disk space using npkill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ashirbadgudu](https://clawhub.ai/user/ashirbadgudu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
JavaScript and Next.js developers use this skill to identify large dependency and build folders and choose cleanup commands that recover disk space in development workspaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cleanup commands can permanently delete dependency or build folders, especially when automated deletion is run from a broad search location. <br>
Mitigation: Prefer dry-run and interactive mode, avoid delete-all from home directories or filesystem root, and review selected paths before deletion. <br>
Risk: The workflow depends on a globally installed npkill npm package. <br>
Mitigation: Verify the npkill package source before global installation and use it only in trusted development environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ashirbadgudu/skills/npkill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can delete local dependency and build folders; dry-run and interactive review are recommended.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
