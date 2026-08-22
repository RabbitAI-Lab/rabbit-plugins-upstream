## Description:

A four-stage coding workflow that guides agents through research, planning, user review, and TDD implementation, with optional PR capture guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to make coding agents produce auditable research and plan files, collect user approval, implement changes with TDD, and prepare PRs with verification evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine status, planning, or domain-keyword prompts may trigger broad local wiki, vector memory, and generated-document searches.

Mitigation: Use the skill only in workspaces where broad prior-art search is acceptable, and review configured output directories and RAG dispatch flags before enabling it on sensitive repositories.

Risk: Workflow steps can lead to issue comments, branch creation, commits, pushes, or PR creation when paired with GitHub workflow tools.

Mitigation: Require explicit user approval before implementation, push, or PR actions, and review linked-issue posting behavior before use on private projects.

Risk: Strict planning and review gates may slow small changes or simple status checks.

Mitigation: Reserve the skill for non-trivial code-change workflows and document when trivial one- or two-line changes may bypass the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [Skill definition](SKILL.md)
- [Workflow steps](steps.md)
- [Implementation workflow](implement.md)
- [Plan and research pre-search](plan-research-search.md)
- [PR workflow](pr.md)
- [Release changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and file-oriented workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct creation of research, plan, task, branch, commit, test, and PR artifacts.]

## Skill Version(s):

0.7.0 (source: server release metadata and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
