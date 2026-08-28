## Description:

Lightweight HTTP endpoint health checks with curl. Use when an agent needs to (1) verify one or more URLs are reachable, (2) collect status codes, TLS info, and timing, or (3) loop-check a service during deployment or incident triage without standing up a full monitoring tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site reliability engineers use this skill to check HTTP(S) endpoint reachability, status codes, TLS handshake details, and timing during deployment or incident triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Endpoint probes contact user-selected hosts from the execution environment and may reveal source IP, timing, and basic request metadata.

Mitigation: Probe only authorized endpoints and account for proxy, VPN, allowlist, and incident-response requirements before running checks.

Risk: Unbounded repeated probes can tie up the foreground session or generate unnecessary traffic.

Mitigation: Use bounded curl timeouts and scheduled checks instead of tight sleep loops for recurring monitoring.

## Reference(s):

- [Scheduling notes for httping](references/scheduling.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks and plain-text probe output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports status codes, remote IPs, TLS verification results, and timing; callers decide health thresholds.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
