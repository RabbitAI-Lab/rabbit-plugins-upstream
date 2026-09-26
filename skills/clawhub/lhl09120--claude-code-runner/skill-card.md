## Description:

Execute programming tasks via Claude Code using PTY-based invocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lhl09120](https://clawhub.ai/user/lhl09120)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to run Claude Code tasks in non-interactive or automated environments, including code review, refactoring, feature implementation, and bug fixes. It is intended for controlled local or CI-style programming workflows where file changes may be synchronized back to a project directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run agent-driven coding tasks with broad local authority and automatic approval of confirmation prompts.

Mitigation: Use it only in disposable or tightly controlled environments, review prompts before execution, and inspect generated changes before trusting or deploying them.

Risk: Security evidence identifies unsafe paths for command injection when prompts or project directories are untrusted.

Mitigation: Do not pass untrusted prompts or project directories until shell construction issues are fixed.

Risk: The skill can write synchronized changes back into the source tree, and security evidence flags privileged file write-back and symlink-safe sync concerns.

Mitigation: Avoid running with root privileges, use version control or disposable copies, and review synchronized files before merging them into important workspaces.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lhl09120/skills/claude-code-runner)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Plain text command output and code or file changes produced by Claude Code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns combined stdout and stderr; successful runs may synchronize generated file changes back to the source project.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
