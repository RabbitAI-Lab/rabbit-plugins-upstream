## Description:

pr0xteus helps trusted self-hosted workloads request operator-approved WireGuard-backed SOCKS5 and HTTP egress through a bearer-protected private API without exposing an open proxy or caller-supplied infrastructure configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to allocate, inspect, and replace private country- or pool-specific proxy exits for trusted services running against an existing pr0xteus controller. It also guides setup and Go client integration while keeping pool policy, WireGuard material, and Docker configuration under operator control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup uses a remote installer that may change between review and execution and can optionally be run with root privileges.

Mitigation: Review the installer at the exact time of use, prefer the per-user path, avoid sudo unless a shared system-wide stack is required, and pin or verify the installer before running it.

Risk: Proxy URLs, WireGuard files, Docker access, and PR0XTEUS_API_TOKEN are sensitive capabilities.

Mitigation: Keep credentials and returned proxy URLs out of logs, issue trackers, and public services; use only trusted private control endpoints and approved destinations.

Risk: Allocating a proxy can consume provider capacity and route traffic through operator-managed egress.

Mitigation: Request only the country, pool, and task the user named, and use operator-approved WireGuard material and routing policy.

## Reference(s):

- [pr0xteus setup](artifact/references/setup.md)
- [pr0xteus project repository](https://github.com/psyb0t/pr0xteus)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pr0xteus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an operator-provided PR0XTEUS_URL and PR0XTEUS_API_TOKEN; returned proxy URLs and token values are sensitive.]

## Skill Version(s):

0.11.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
