## Description:

Debug Python with pdb, breakpoint(), post-mortem inspection, and debugpy remote attach.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and apply Python debugging workflows for local scripts, failing tests, long-running services, and remote or headless attach scenarios.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A debugpy listener can expose an interactive debugging interface if bound beyond localhost.

Mitigation: Bind debug servers to 127.0.0.1 and use isolation or tunneling before considering any non-local exposure.

Risk: PID attach behaves like debugger injection and can affect sensitive or production processes.

Mitigation: Attach only to approved targets, avoid production and security-sensitive processes unless explicitly authorized, and confirm required ptrace or container privileges before changing the target.

Risk: Debugger statements or debugpy setup can be accidentally committed after troubleshooting.

Mitigation: Search for breakpoint(), pdb.set_trace, and debugpy references before commit, then rerun the normal project test or release gate without the debugger.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/python-debugpy)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; may suggest installing debugpy in the active Python environment.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
