## Description: <br>
Autonomous orchestrator for manifest work items through the development lifecycle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to process manifest-backed work items through intake, build, quality, and ship stages. It is designed for autonomous backlog processing with state transitions, retries, budget checks, and optional PR preparation or merge steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can drive broad repository changes through an autonomous development pipeline. <br>
Mitigation: Install it only in repositories where autonomous backlog processing is intentional, and review `.egregore` configuration before launch. <br>
Risk: Automatic merge behavior can reduce human control over repository changes. <br>
Mitigation: Keep `auto_merge` disabled unless the workflow is trusted and monitored. <br>
Risk: Recurring self-relaunch or cron behavior can keep work running longer than expected. <br>
Mitigation: Avoid durable cron use unless needed, and monitor scheduled tasks, branches, worktrees, and pull requests during runs. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/athola/skills/nm-egregore-summon) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/egregore) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline code blocks and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide updates to manifest, budget, continuation, branch, worktree, and PR state during orchestrated runs.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence and release changelog; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
