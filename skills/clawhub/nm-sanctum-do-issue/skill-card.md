## Description: <br>
Implements GitHub or GitLab issues via parallel subagents with review gates between task batches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to fetch GitHub or GitLab issues, break them into implementation tasks, run independent work in parallel where appropriate, review batches, and consolidate the result into one pull request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can make persistent remote changes through authenticated GitHub or GitLab access, including comments, issue closure, commits, and pull request preparation. <br>
Mitigation: Confirm the target repository and issues before use, review generated comments or closure actions before posting, and keep automatic closure disabled unless explicitly approved. <br>
Risk: The workflow can ask the agent to post tooling feedback to an unrelated public Night Market repository. <br>
Mitigation: Skip that feedback step unless the user explicitly approves it and the content has been reviewed and sanitized. <br>
Risk: Parallel subagent execution can create coordination failures, merge conflicts, or hard-to-monitor changes. <br>
Mitigation: Use the documented planning threshold for larger dispatches, review each batch before proceeding, and fall back to sequential execution when tasks share files or high-risk changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-sanctum-do-issue) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Issue Discovery](modules/issue-discovery.md) <br>
- [Task Planning](modules/task-planning.md) <br>
- [Parallel Execution](modules/parallel-execution.md) <br>
- [Quality Gates](modules/quality-gates.md) <br>
- [Completion](modules/completion.md) <br>
- [Troubleshooting](modules/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate issue comments, issue closure, commits, and pull request preparation through authenticated forge CLIs.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter: 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
