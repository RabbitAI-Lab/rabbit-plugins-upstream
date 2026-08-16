## Description:

Give a trusted self-hosted workload a configured WireGuard-backed SOCKS5 exit through pr0xteus's bearer-protected private HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect trusted self-hosted workloads to operator-approved country or pool based SOCKS5 egress through a private pr0xteus controller. It also helps inspect pool state, replace failed proxy assignments, and integrate the Go client while keeping tokens, WireGuard bundles, and private proxy URLs scoped to trusted environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer tokens, WireGuard files, and returned SOCKS5 URLs are private secrets.

Mitigation: Use operator-supplied environment variables or a secret store, avoid searching local files for credentials, and do not expose returned proxy URLs outside the intended private Docker network.

Risk: Installer and Docker setup can affect host configuration and shared operator access.

Mitigation: Inspect the installer before running it, prefer per-user setup unless a shared system-wide stack is intended, and pin released images unless an operator explicitly chooses rolling behavior.

Risk: Allocating a proxy can consume provider capacity and route workload traffic through operator-controlled egress.

Mitigation: Request only the user-approved country or logical pool for the named task and use the private controller only from trusted workloads.

## Reference(s):

- [pr0xteus setup](artifact/references/setup.md)
- [pr0xteus ClawHub release](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [pr0xteus project homepage](https://github.com/psyb0t/pr0xteus)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, YAML, and Go snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a trusted PR0XTEUS_URL, PR0XTEUS_API_TOKEN, and local bash, curl, docker, and jq for setup or verification commands.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
