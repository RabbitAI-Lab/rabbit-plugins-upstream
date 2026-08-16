## Description:

Monitors hosts, phones, and daemon processes with ICMP reachability checks and returns status-oriented monitoring results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operations teams, and automation workflows use this skill to check ICMP reachability for hosts, phones, or daemon endpoints and review status or alert-style results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the artifact suspicious because it requests command execution and describes broader automation, file, API, and workflow behavior than a narrow ping monitor requires.

Mitigation: Use it only for explicit, authorized ping or ICMP reachability checks; avoid broad command execution or file access unless local diagnostics are intended.

Risk: ICMP monitoring can be misused against networks or devices that the user is not authorized to test.

Mitigation: Limit targets to systems the operator owns or is explicitly permitted to monitor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ping-monitor)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional shell commands and JSON status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit monitoring targets and should be limited to authorized ICMP reachability checks.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
