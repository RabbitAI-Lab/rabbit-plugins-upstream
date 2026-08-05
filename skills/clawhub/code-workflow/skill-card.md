## Description: <br>
Code Workflow guides coding agents through a four-stage research, planning, user-review, and TDD implementation process for code changes, issue work, and pull requests with optional visual evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to structure moderate or complex code changes: research the repository, write auditable plans, obtain explicit user review, implement with TDD, and prepare pull requests with supporting evidence when requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward persistent repository changes such as plans, local indexes, branches, commits, issue comments, and pull requests. <br>
Mitigation: Use it only in repositories where that level of agent authority is intended, and review plans before they are committed, posted, or used to start implementation. <br>
Risk: Plan or research artifacts may contain private implementation details and can be routed to external memory or indexing receivers when optional RAG dispatch is enabled. <br>
Mitigation: Avoid the optional RAG dispatch flag unless the receiver is trusted for the repository data, and keep sensitive projects on local file artifacts when possible. <br>
Risk: GitHub issue comments, pull request bodies, and visual attachments may expose internal context outside the local workspace. <br>
Mitigation: Require explicit user intent before posting externally or creating a pull request, and review generated content and captures for sensitive details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Research, plan, review, and branch workflow](artifact/steps.md) <br>
- [TDD implementation workflow](artifact/implement.md) <br>
- [PR workflow with visual evidence](artifact/pr.md) <br>
- [Plan and research pre-search obligation](artifact/plan-research-search.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, checklists, code snippets, and PR body templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead an agent to create or update workspace research files, plan files, task checklists, branches, commits, GitHub issue comments, and pull request content.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata and CHANGELOG, released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
