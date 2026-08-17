## Description:

Give a trusted self-hosted workload a configured WireGuard-backed SOCKS5 exit through pr0xteus's bearer-protected private HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure, inspect, and operate a trusted private pr0xteus controller for country-specific SOCKS5 egress through operator-owned WireGuard cells. It supports proxy allocation, pool and cell inspection, bad-assignment replacement, and Docker-based setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide allocation of Docker-backed WireGuard cells and return SOCKS5 bearer URLs that route traffic through operator-controlled egress.

Mitigation: Use only trusted private control endpoints, keep PR0XTEUS_API_TOKEN and returned proxy URLs out of logs, and request only the country, pool, and task the user named.

Risk: Setup and lifecycle commands can affect Docker containers and local pr0xteus configuration.

Mitigation: Inspect the installer before running it, use authorized WireGuard material, and keep teardown limited to cells intentionally selected by the operator or user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [pr0xteus project homepage](https://github.com/psyb0t/pr0xteus)
- [Setup reference](references/setup.md)
- [Installer script](https://raw.githubusercontent.com/psyb0t/pr0xteus/main/install.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash, curl, Docker, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses operator-supplied PR0XTEUS_URL and PR0XTEUS_API_TOKEN; returned SOCKS5 URLs are short-lived bearer capabilities.]

## Skill Version(s):

0.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
