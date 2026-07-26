## Description: <br>
Activate a 4-stage coding discipline framework that forces Claude to plan before coding, isolate changes on a branch, write tests first, and self-review output twice before presenting it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to make coding agents follow a stricter delivery workflow for complex tasks: confirm a plan, isolate changes, write tests first, and complete a double review before presenting results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may activate on broad coding requests and slow work by requiring explicit planning, test-first steps, and review checkpoints. <br>
Mitigation: Use it when a stricter coding workflow is desired, and clarify when a task should skip or narrow the full process. <br>
Risk: The skill may create feature branches while isolating changes. <br>
Mitigation: Review the announced branch name and changed files before merging or treating the work as final. <br>
Risk: The skill suggests CLAUDE.md text for permanent project use. <br>
Mitigation: Add that text only when the project should always enforce this workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/claude-superpowers) <br>
- [Project Skill Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/claude-superpowers.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with structured checklists and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a written plan, branch name, test summary, review checklist, completion summary, and optional CLAUDE.md installation text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
