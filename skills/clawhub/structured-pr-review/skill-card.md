## Description: <br>
Layered PR code review with severity tiers (MUST FIX/SHOULD FIX/SUGGESTION) and addressing-mode. Default: gh CLI only; optional Lobster pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ggettert](https://clawhub.ai/user/ggettert) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to review GitHub pull requests through layered security, correctness, conventions, infrastructure, and testing checks. It can also help address review feedback by proposing or applying code changes, replies, thread resolutions, PR description updates, and pushes when explicitly used in addressing mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Addressing mode can modify a pull request through commits, replies, thread resolution, PR description edits, and pushes. <br>
Mitigation: Confirm the target repository, branch, generated code changes, comments, thread resolutions, and PR description edits before pushing or posting through gh. <br>
Risk: Review findings or suggested fixes may be incomplete or incorrect for the target codebase. <br>
Mitigation: Use the skill output as review assistance and validate findings, CI state, and proposed changes before merge or deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ggettert/skills/structured-pr-review) <br>
- [Server-Resolved GitHub Source](https://github.com/ggettert/openclaw-skills/tree/main/structured-pr-review) <br>
- [Lobster Integration](references/lobster-integration.md) <br>
- [Review Layers](references/review-layers.md) <br>
- [Addressing Workflow](references/addressing-workflow.md) <br>
- [Team Conventions](references/conventions.md) <br>
- [Infrastructure as Code Checklist](references/iac-checklist.md) <br>
- [GitHub CLI](https://cli.github.com) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown review findings and action summaries, JSON PR context envelopes, and inline shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The data-gathering scripts emit a pr-context-v0 JSON envelope; addressing mode may produce repository changes, GitHub replies, thread resolutions, PR description edits, and pushes.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
