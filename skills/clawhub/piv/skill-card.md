## Description: <br>
PIV orchestrates a Plan, Implement, Validate workflow for phase-based software development with PRDs, PRPs, codebase analysis, implementation, validation, and debugging loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smokealot420](https://clawhub.ai/user/smokealot420) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate multi-phase implementation work from requirements through PRP generation, execution, validation, debugging, and local commit preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify repository files and prepare local commits as part of an autonomous implementation workflow. <br>
Mitigation: Use it only in trusted repositories and inspect git status and diffs before accepting changes or commits. <br>
Risk: Generated PRPs or validation commands may be incorrect or inappropriate for the target project. <br>
Mitigation: Review PRPs before execution and inspect validation commands before allowing them to run. <br>
Risk: Sub-agent execution can run project commands and change code without strong built-in confirmation or command scoping. <br>
Mitigation: Limit use to repositories where command execution is acceptable and review execution summaries, validation reports, and resulting file changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smokealot420/skills/piv) <br>
- [Project homepage](https://github.com/SmokeAlot420/ftw) <br>
- [Codebase analysis reference](references/codebase-analysis.md) <br>
- [PRD creation reference](references/create-prd.md) <br>
- [PRP generation reference](references/generate-prp.md) <br>
- [PRP execution reference](references/execute-prp.md) <br>
- [PIV executor reference](references/piv-executor.md) <br>
- [PIV validator reference](references/piv-validator.md) <br>
- [PIV debugger reference](references/piv-debugger.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured agent reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project planning files, workflow trackers, implementation files, validation reports, and local commits when used in a repository.] <br>

## Skill Version(s): <br>
1.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
