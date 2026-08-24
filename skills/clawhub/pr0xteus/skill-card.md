## Description:

pr0xteus guides agents through operating a trusted private controller that allocates WireGuard-backed SOCKS5 exits, inspects pools and cells, replaces failed assignments, and integrates Go clients without exposing an open proxy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect trusted self-hosted workloads to operator-approved country or pool exits through a private pr0xteus control API. It helps them check health and pool state, allocate or replace SOCKS5 assignments, inspect live cells, and follow the documented Docker-backed setup path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide allocation of proxy capacity and route traffic through operator-controlled WireGuard exits.

Mitigation: Use only trusted private controllers and request only operator-approved countries, pools, and destinations.

Risk: Bearer tokens and returned SOCKS5 URLs can grant access to the control API or gateway if exposed.

Mitigation: Keep PR0XTEUS_API_TOKEN and returned proxy URLs out of logs, tickets, public services, and generated artifacts.

Risk: Setup and cell operations can start Docker-backed infrastructure or stop active pr0xteus cells.

Mitigation: Inspect the installer before running it and require explicit user intent before teardown actions.

## Reference(s):

- [pr0xteus ClawHub page](https://clawhub.ai/psyb0t/skills/pr0xteus)
- [pr0xteus homepage](https://github.com/psyb0t/pr0xteus)
- [pr0xteus setup](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, YAML, and Go-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses PR0XTEUS_URL and PR0XTEUS_API_TOKEN supplied by the operator; returned SOCKS5 URLs should be treated as short-lived bearer credentials.]

## Skill Version(s):

0.10.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
