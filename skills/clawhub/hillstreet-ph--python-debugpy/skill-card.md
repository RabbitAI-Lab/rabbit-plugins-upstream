## Description:

Debug Python with pdb, breakpoint(), post-mortem inspection, and debugpy remote attach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Python program state, investigate exceptions and failing tests, and attach a debugger to running or remote processes. It guides them in choosing pdb, breakpoint(), post-mortem inspection, or debugpy based on the debugging task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remotely accessible debug server can expose control over the target process.

Mitigation: Bind debug servers to 127.0.0.1; use a tunnel or isolated network when remote access is needed.

Risk: Attaching by PID can affect an unintended running process.

Mitigation: Confirm the target PID before attaching.

Risk: Temporary breakpoints or debugger hooks can be left in project code after investigation.

Mitigation: Search for debugger calls, remove temporary hooks, then rerun the normal project test or gate.

## Reference(s):

- [python-debugpy on ClawHub](https://clawhub.ai/hillstreet-ph/skills/python-debugpy)
- [Publisher profile: hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with shell commands and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and commands are selected for the user's Python process and debugging scenario.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
