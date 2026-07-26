## Description: <br>
Loop engineering CLI v0.4.4 with project intake, adaptive queues, progress reports, and human gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ambitioncn](https://clawhub.ai/user/ambitioncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to manage explicit loop-engineering workflows for project intake, queue setup, adaptive queue execution, progress reporting, and review-gated code worktree handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queue dispatcher commands and cron entries can run local workflows in the target workspace. <br>
Mitigation: Review queue configs, dispatcher commands, and cron entries before execution; start with manual ticks and inspect generated run artifacts before scheduling recurring runs. <br>
Risk: Commands using `--confirm-apply` or `--confirm-cleanup` can change local files or remove reviewed worktrees. <br>
Mitigation: Use the read-only planning, status, review bundle, patch verification, and cleanup-plan commands first, and supply confirmation flags only after human review. <br>
Risk: High-risk process-control, live instrumentation, publishing, destructive, credential, or production configuration actions may exceed ordinary loop automation expectations. <br>
Mitigation: Keep those actions separately gated and stop at artifacts for human review unless the user explicitly approves execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ambitioncn/skills/loop-engineering) <br>
- [NPM Package Reference](references/npm-package.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and artifact paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local loop configuration, queue state, status ledgers, review bundles, patches, and closeout artifacts when the user explicitly runs the corresponding CLI commands.] <br>

## Skill Version(s): <br>
0.4.4 (source: server release evidence and package reference, released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
