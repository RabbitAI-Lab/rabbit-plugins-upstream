## Description:

Code Workflow guides agents through a research, planning, user review, and TDD implementation process for code changes, with optional pull request preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to structure code-change work from context discovery through reviewed plans, TDD implementation, and optional PR evidence capture. It is intended for issue implementation, tracked tasks, new features, and code-change workflows that benefit from explicit checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can search prior plans, memory stores, wiki content, and peer documentation, which may pull in cross-project or stale context.

Mitigation: Restrict search roots to the active repository and review retrieved context before using it in plans or implementation.

Risk: Plan-to-issue, RAG dispatch, or PR-related steps can publish or send work artifacts outside the local session.

Mitigation: Require an explicit preview and user confirmation before posting to GitHub, dispatching to memory or indexing receivers, pushing, or opening a PR.

Risk: Hook scripts may inspect workflow activity and enforce guardrails in the user's agent environment.

Mitigation: Review any hook installation, especially under ~/.claude/hooks, before enabling the workflow.

## Reference(s):

- [Code Workflow ClawHub page](https://clawhub.ai/drumrobot/skills/code-workflow)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, command snippets, and workflow artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce research, plan, walkthrough, implementation, and PR preparation artifacts depending on the invoked topic.]

## Skill Version(s):

0.9.1 (source: server release metadata and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
