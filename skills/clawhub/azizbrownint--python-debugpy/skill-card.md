## Description:

Debug Python with pdb, breakpoint(), post-mortem inspection, and debugpy remote attach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and run an appropriate Python debugger for local, post-mortem, remote, headless, or already-running process debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing debugpy as a fallback can introduce an unreviewed dependency into the active environment.

Mitigation: Install debugpy in an isolated virtual environment when possible and pin a reviewed version.

Risk: Remote debug servers and PID attach can expose or manipulate live process state.

Mitigation: Bind debug servers to localhost and attach only to processes the user owns or has explicit approval to inspect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/python-debugpy)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; includes local debugger commands and debugpy remote attach patterns.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
