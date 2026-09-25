## Description:

Use when implementation is complete, all tests pass, and you need to decide how to integrate the work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill after implementation is complete and tests pass to choose how to integrate a development branch, create a pull request, preserve the branch, or perform explicitly confirmed cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can lead an agent to propose real repository changes, including merge, push, pull request creation, worktree cleanup, and branch deletion.

Mitigation: The skill requires a passing test suite, explicit user menu selection, and typed confirmation before destructive discard operations.

Risk: Merging into the wrong base branch can be costly to undo.

Mitigation: The skill directs the agent to determine or confirm the base branch before any merge action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/finishing-a-development-branch)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown guidance with menu text and inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires test verification and explicit user choices before merge, push, pull request creation, worktree cleanup, or branch deletion.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
