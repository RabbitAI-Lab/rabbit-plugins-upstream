## Description:

Agentic software development methodology covering brainstorming, planning, test-driven development, debugging, code review, git worktrees, and branch management for disciplined AI-assisted software work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cutd](https://clawhub.ai/user/cutd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to guide agents through structured software workflows such as design, implementation planning, TDD, debugging, review, worktree setup, and branch completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may steer agents toward sensitive repository actions such as commits, pushes, pull requests, branch cleanup, worktree creation, dependency installation, or repository-controlled build and test execution.

Mitigation: Require explicit user approval for those actions and review the exact command or operation before execution.

Risk: A workflow skill could be misapplied as authority to override the current user request, project instructions, or host safety policy.

Mitigation: Treat the skill as guidance only; current user instructions, project instructions, and host policy remain authoritative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cutd/skills/claw-superpowers)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with checklists, command examples, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-only skill; no API keys, MCP tools, or executable scripts detected in the artifact.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
