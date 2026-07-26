## Description: <br>
Implements file-based planning so agents can organize complex work with persistent task plans, findings, progress logs, reusable scripts, and session recovery support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[othmanadi](https://clawhub.ai/user/othmanadi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to keep multi-step tasks, research, and implementation work organized across long sessions. It creates and maintains markdown planning files in the user project, with helper scripts for initialization, active-plan selection, progress summaries, completion checks, and session catch-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic hooks can inject persistent planning content into agent turns. <br>
Mitigation: Review the planning files before use, keep plan directories scoped to the current project, and use attestation when relying on automatic injection or gated workflows. <br>
Risk: Session catch-up can read local agent session history for the current project. <br>
Mitigation: Avoid using the skill in projects where prompts, command arguments, or prior tool output may contain secrets. <br>
Risk: Completion-gated workflows may affect when an agent stops. <br>
Mitigation: Use gated mode only when the plan file is expected to be the completion source of truth, and keep phase status current in task_plan.md. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files) <br>
- [Planning with Files reference](references/reference.md) <br>
- [Planning with Files examples](references/examples.md) <br>
- [Manus context engineering article](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown files with inline shell and PowerShell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates task_plan.md, findings.md, progress.md, and optional .planning plan directories in the user project.] <br>

## Skill Version(s): <br>
3.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
