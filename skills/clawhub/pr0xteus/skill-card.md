## Description:

pr0xteus helps agents allocate and inspect bearer-protected, WireGuard-backed SOCKS5 egress for trusted self-hosted workloads through an operator-owned private HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to give trusted self-hosted services an operator-approved country or pool-specific SOCKS5 exit, inspect pr0xteus pools, replace failed proxy assignments, and integrate the Go client with controlled retry behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run an installer with sudo and start Docker-backed networking components.

Mitigation: Review the installer before execution and proceed only when operating a trusted pr0xteus controller with authorized WireGuard material.

Risk: A returned SOCKS5 URL routes traffic through private egress infrastructure and can be misused if exposed outside the intended workload.

Mitigation: Keep returned SOCKS5 URLs inside the private Docker network and use them only for the task, country, or pool the user requested.

Risk: Proxy allocation can consume provider capacity and change the workload's apparent exit country.

Mitigation: Request only operator-approved countries or pools and avoid scanning workspaces or host paths for tokens, WireGuard bundles, or Docker configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [pr0xteus project homepage](https://github.com/psyb0t/pr0xteus)
- [Setup guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, curl, YAML, and Go client examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bearer-authenticated HTTP API calls and Docker commands for operator-approved setup or verification.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
