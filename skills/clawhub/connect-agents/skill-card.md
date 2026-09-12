## Description:

Connect agents over A2A by configuring agent cards, bearer tokens, reachability, HTTPS, and troubleshooting checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samorodkin](https://clawhub.ai/user/samorodkin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to connect agents over A2A and diagnose setup failures involving inbound listeners, bearer tokens, hostnames, HTTPS advertisement, stable addresses, and network reachability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing an inbound A2A listener can make an agent reachable over a network.

Mitigation: Expose inbound A2A only intentionally, require bearer-token authentication, and avoid broadly sharing agent-card URLs or tokens.

Risk: A misadvertised http URL behind a TLS proxy can cause bearer tokens to be sent without HTTPS protection.

Mitigation: Confirm the published agent card advertises HTTPS and set the public URL explicitly when proxy headers are unreliable.

Risk: Rotating deployment hostnames or bearer tokens can silently break peer configurations after restarts.

Mitigation: Use stable hostnames and persistent tokens, and record the peer name, URL, and token storage location for future debugging.

## Reference(s):

- [Connect agents over A2A on ClawHub](https://clawhub.ai/samorodkin/skills/connect-agents)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and troubleshooting checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance only; it does not install, execute, or hide behavior.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
