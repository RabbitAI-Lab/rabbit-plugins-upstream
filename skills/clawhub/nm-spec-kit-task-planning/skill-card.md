## Description: <br>
Generates phased, dependency-ordered implementation tasks from specifications after a spec is complete and before implementation begins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to turn specifications and implementation plans into phased task lists with explicit dependencies, file ownership, verification criteria, and safe parallelization markers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked by generic planning-related terms, so an agent could apply it when a user did not intend a full implementation task breakdown. <br>
Mitigation: Confirm the user wants task planning before generating or acting on a phased task list. <br>
Risk: Generated task lists can include installs, git operations, or production changes that carry operational risk if executed without review. <br>
Mitigation: Review generated tasks and commands before execution, especially for dependency installation, repository changes, or production-impacting work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-spec-kit-task-planning) <br>
- [OpenClaw metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/spec-kit) <br>
- [Task phase structure](artifact/modules/phase-structure.md) <br>
- [Task dependency patterns](artifact/modules/dependency-patterns.md) <br>
- [Technology stack patterns](artifact/modules/tech-stack-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown task plan with task IDs, phases, dependencies, file paths, criteria, and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include parallel markers for independent tasks and quality checklist items for review.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata; skill frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
