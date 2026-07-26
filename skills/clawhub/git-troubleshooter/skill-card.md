## Description: <br>
Diagnose a tangled git situation and give the exact, safe commands to fix it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to diagnose common Git problems and receive safe, ordered recovery commands with explanations and an undo path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Git commands may discard work or rewrite history if applied without review. <br>
Mitigation: Review commands before execution, keep the suggested safety branch or reflog recovery step, and use extra caution with reset, clean, rebase, and force-push commands. <br>
Risk: The skill may need to infer repository state from incomplete user descriptions. <br>
Mitigation: Confirm assumptions against the intended repository and provided git status or error output before running the fix. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/git-troubleshooter) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/git-troubleshooter.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Guidance] <br>
**Output Format:** [Markdown with numbered command sequences and inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes diagnosis, command explanations, safety warnings, and recovery notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
