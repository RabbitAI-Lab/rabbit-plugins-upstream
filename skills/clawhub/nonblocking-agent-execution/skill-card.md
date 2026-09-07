## Description:

Enhanced Non-Blocking Agent Execution helps agents avoid stuck or silent long-running tool calls by using a detach, bounded-poll, and durable-state pattern with a ready-to-use job controller.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to launch, monitor, poll, verify, debug, and clean up long-running shell jobs without blocking an agent turn. It is intended for local or sandboxed workflows where durable job state and bounded polling reduce the risk of stalled sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The job runner executes user-provided shell commands and can persist job state and logs.

Mitigation: Use it only in trusted local or sandboxed environments, validate commands before launch, run with least privilege, and restrict permissions on ~/.nonblocking.

Risk: Callback URLs can send job output outside the local machine.

Mitigation: Avoid callbacks for sensitive output, require HTTPS endpoints, and review callback destinations before use.

Risk: Background jobs and retained state can accumulate or continue longer than expected.

Mitigation: Set explicit runtime limits, poll status, clean up completed jobs regularly, and verify the installed artifact before making scripts executable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/nonblocking-agent-execution)
- [README](README.md)
- [API Documentation](docs/API.md)
- [Integration Guide](docs/INTEGRATION.md)
- [Best Practices Guide](docs/BEST_PRACTICES.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON status examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local job state, logs, output files, and optional callback payloads when configured.]

## Skill Version(s):

2.0.2 (source: server release metadata; artifact frontmatter reports 2.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
