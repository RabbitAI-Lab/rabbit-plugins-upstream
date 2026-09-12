## Description:

Operate an IMesh Python mesh for discovering trusted peers, starting a local node, calling remote skills, and checking mesh health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lafouine69](https://clawhub.ai/user/lafouine69)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate a local-first IMesh agent mesh from a shell, including peer discovery, local node startup, trusted remote skill calls, and gateway health checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Binding IMesh services to public interfaces can expose nodes or gateway access beyond local testing.

Mitigation: Keep WAN disabled and bind to 127.0.0.1 unless the operator deliberately confirms use of 0.0.0.0 or a public address.

Risk: Weak or missing shared secrets can allow untrusted peer access or rejected task requests.

Mitigation: Set OPENCLAW_PSK to a long random secret before connecting peers, and expose remote skills only when the peer is trusted and the skill is registered with expose_remote=True.

Risk: Operational output or troubleshooting can leak private keys, API keys, .env files, or gateway database contents.

Mitigation: Do not print, copy, or commit secrets, .env files, private keys, API keys, or gateway database data.

## Reference(s):

- [ClawHub IMesh skill page](https://clawhub.ai/lafouine69/skills/imesh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and environment variable examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational steps for local node management, peer discovery, remote skill calls, gateway checks, and troubleshooting.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
