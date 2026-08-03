## Description: <br>
Complete planning toolkit for requirements specification, task planning, iterative execution, and autonomous cleanup workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to turn ambiguous work into structured requirements, vertical task plans, persistent planning records, and bounded iterative execution loops. It is suited to feature work, multi-file changes, architecture decisions, and longer tasks that benefit from explicit checkpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent planning files may capture sensitive project context if users include it in task plans, findings, or progress logs. <br>
Mitigation: Review generated planning artifacts before sharing or committing them, and avoid placing secrets or sensitive data in planning notes. <br>
Risk: Iterative loop modes can guide repeated local work and state updates. <br>
Mitigation: Use clear stopping criteria, bounded iteration counts, and review loop state before continuing long-running or cleanup-oriented workflows. <br>
Risk: The planning initializer writes local files under .planning and updates .planning/.active_plan. <br>
Mitigation: Use unique task slugs and inspect the planned file locations before running initialization in repositories with existing planning artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/planning-toolkit) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell/Python command output, planning templates, and JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local .planning directories, Markdown planning artifacts, an .active_plan pointer, and loop state JSON when users run the bundled scripts.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
