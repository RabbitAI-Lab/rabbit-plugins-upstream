## Description:

Enforces fresh verification evidence before an agent claims tests pass, a bug is fixed, work is done, or a branch is ready to merge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this discipline skill to require fresh, claim-matched verification before reporting completion, handing off work, committing, pushing, or opening a PR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make agents more conservative around dirty git state, commits, pushes, and broad-scope edits.

Mitigation: Scope verification to the exact claim, run project-specific commands when available, and report concrete blockers or residual risks when verification cannot be completed.

Risk: The skill may prompt agents to run shell commands as verification evidence.

Mitigation: Review proposed commands for authorization and repository relevance before execution, especially before commits, pushes, or release handoffs.

## Reference(s):

- [Isolated Verification](artifact/references/isolated-verification.md)
- [System-Wide Test Check](artifact/references/system-wide-test-check.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fresh command output before completion claims; does not produce files by itself.]

## Skill Version(s):

4.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
