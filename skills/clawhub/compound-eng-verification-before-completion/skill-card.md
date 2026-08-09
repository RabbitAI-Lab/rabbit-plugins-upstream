## Description: <br>
Enforces fresh verification evidence before an agent claims tests pass, a bug is fixed, work is done, a branch is ready, or scope is clear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to require fresh verification evidence before completion, release, or handoff claims. It is especially useful when tests, builds, bug fixes, scope coverage, or delegated work need to be confirmed before reporting success. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to run project verification commands such as tests, builds, local servers, git status checks, temporary worktrees, or migration dry runs. <br>
Mitigation: Review high-impact commands before allowing them, especially commands that affect migrations, local services, repository state, or production-like data. <br>
Risk: Fresh verification requirements can increase task time or expose pre-existing project failures. <br>
Mitigation: Have the agent report the exact failing command and evidence, and separate current-change failures from documented baseline or environment failures before accepting completion claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-verification-before-completion) <br>
- [Isolated Verification](references/isolated-verification.md) <br>
- [System-Wide Test Check](references/system-wide-test-check.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands and verification report structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs the agent to run and read project-specific verification commands before making completion claims.] <br>

## Skill Version(s): <br>
4.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
