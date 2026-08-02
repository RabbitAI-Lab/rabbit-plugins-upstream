## Description: <br>
Agentspace helps developers share a named development folder as a live browser workspace so reviewers or other agents can inspect generated files, logs, build output, screenshots, and test artifacts during agent development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[permew](https://clawhub.ai/user/permew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to start, share, and review live development workspaces for agent runs, including debugging generated code, reviewing build and test output, and handing off work between people or agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload the user-named development folder to agentspace.so. <br>
Mitigation: Confirm the exact folder path before running sync or share, and avoid sharing folders that contain secrets, credentials, or unrelated private files. <br>
Risk: View or edit share links and .ascli.json binding data can grant workspace access. <br>
Mitigation: Treat edit links and .ascli.json as workspace access material, prefer view-only links for review, and share them only with intended recipients. <br>


## Reference(s): <br>
- [Agentspace homepage](https://agentspace.so) <br>
- [Agentspace skill on ClawHub](https://clawhub.ai/permew/skills/agentspace-dev) <br>
- [Agentspace skills repository](https://github.com/agentspace-so/skills) <br>
- [npm @agentspace-so/ascli](https://www.npmjs.com/package/@agentspace-so/ascli) <br>
- [Agent Space Commands](references/commands.md) <br>
- [Developer reference for agentspace dev sessions](references/developer.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and returned workspace URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should use only URLs printed by ascli and should name the exact folder path before sync or share commands run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
