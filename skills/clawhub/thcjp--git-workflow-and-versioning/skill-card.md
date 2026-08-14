## Description:

Helps developers structure Git workflow and versioning tasks, including commits, branches, conflict handling, merges, rollback, and release coordination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to plan and carry out Git version-control workflows, including branch management, commits, merges, conflict handling, tagging, rollback, and release coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution for broad Git automation, including workflows that can change repository state.

Mitigation: Use it only for explicit version-control tasks and require confirmation before commit, branch, merge, tag, rollback, or push actions.

Risk: Repository content or credentials could be exposed if external services or API tokens are used without review.

Mitigation: Require confirmation before API-token use or sending repository content to any external service.

Risk: Overly broad automatic activation language may cause the skill to be invoked for unrelated code changes.

Mitigation: Review the skill before installing and activate it only when Git workflow or versioning assistance is explicitly needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/git-workflow-and-versioning)
- [Skill homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose repository-changing Git actions that require user review before execution.]

## Skill Version(s):

1.0.0 (source: evidence.release.version, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
