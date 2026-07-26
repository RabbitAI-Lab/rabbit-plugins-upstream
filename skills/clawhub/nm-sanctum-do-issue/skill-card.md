## Description: <br>
Implements GitHub or GitLab issues via parallel subagents with review gates between task batches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to fetch GitHub or GitLab issues, break them into tasks, execute independent work in parallel, review batches, and consolidate completed issue work into one pull request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use authenticated GitHub or GitLab CLI access to read issues, change code, commit work, comment on issues, close issues, or create a pull request. <br>
Mitigation: Run it only in repositories where that level of agent access is acceptable, and review proposed issue comments, closures, commits, and pull requests before they are published. <br>
Risk: The workflow includes an external public feedback step for tooling observations that could expose project details without clear confirmation. <br>
Mitigation: Disable that step or require explicit manual approval before posting any tooling feedback outside the current repository. <br>
Risk: Parallel subagent execution can create merge conflicts, incomplete work, or hard-to-recover hangs in remote-control or headless sessions. <br>
Mitigation: Use the documented review gates, keep high-risk or dependent tasks sequential, limit parallelism, and prefer local sessions when subagents are required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-do-issue) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>
- [Claude Code issue #28482](https://github.com/anthropics/claude-code/issues/28482) <br>
- [Claude Code issue #33232](https://github.com/anthropics/claude-code/issues/33232) <br>
- [Claude Code issue #13240](https://github.com/anthropics/claude-code/issues/13240) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, issue workflow steps, task prompts, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to read and comment on issues, modify code, run tests, commit changes, and prepare one consolidated pull request.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
