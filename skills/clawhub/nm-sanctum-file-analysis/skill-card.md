## Description: <br>
Maps file structure and module organization of a codebase before architecture reviews, refactoring planning, or migration scope estimation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to map repository layout, module organization, file distributions, and likely complexity hotspots before architecture review, refactoring, or migration planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may enumerate file and directory names in the active workspace. <br>
Mitigation: Use it only in workspaces where repository structure can be shared with the active agent and review outputs before redistribution. <br>
Risk: Broad activation triggers could make the skill run for some general file-related requests. <br>
Mitigation: Confirm the task is repository structure analysis before using the skill's workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-file-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [ClawHub metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with repository observations and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes file counts, directory layout notes, and hotspot observations when applied to a workspace.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
