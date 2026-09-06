## Description:

Enforces fresh verification evidence before any completion claim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to require fresh, claim-matched verification evidence before reporting tests, fixes, handoffs, or completion. It helps keep partial, stale, refusal-only, or weakened-proof outcomes visible instead of overstated.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can increase local verification activity, including tests, builds, git status or diff checks, endpoint probes, temporary worktrees, and scratch ledgers.

Mitigation: Review proposed commands before allowing execution in sensitive repositories, especially commands that affect commits, stashes, infrastructure dry runs, or local worktrees.

Risk: Agents may overstate completion if verification evidence is stale, partial, or matched to the wrong claim.

Mitigation: Require fresh command output for the specific claim being made and state any narrower verification scope or unavailable automated checks.

## Reference(s):

- [Isolated Verification](references/isolated-verification.md)
- [System-Wide Test Check](references/system-wide-test-check.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, text]

**Output Format:** [Markdown guidance with inline command examples and verification checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May increase local verification activity such as tests, builds, git status or diff checks, endpoint probes, temporary worktrees, and scratch ledgers.]

## Skill Version(s):

4.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
