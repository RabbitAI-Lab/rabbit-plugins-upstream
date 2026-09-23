## Description:

ICMP health check for hosts, phones, and daemons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xejrax](https://clawhub.ai/user/xejrax)

### License/Terms of Use:


## Use Case:

Developers and operators use this skill to check whether hosts, phones, or daemons are reachable with the system ping utility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ping-style reachability checks can be logged or restricted and may be inappropriate against hosts or networks the user does not control.

Mitigation: Run the skill only against hosts and networks the user owns or has permission to test.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xejrax/skills/ping-monitor)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the system ping binary.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
