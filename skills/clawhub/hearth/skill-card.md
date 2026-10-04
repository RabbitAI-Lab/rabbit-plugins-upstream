## Description:

Hearth performs read-only health sweeps across configured homelab devices and reports connectivity, resource usage, service status, and application health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nj070574-gif](https://clawhub.ai/user/nj070574-gif)

### License/Terms of Use:

MIT-0

## Use Case:

Homelab administrators and developers use this skill to check configured devices for outages and degraded health, then review per-device results without changing remote hosts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disabled SSH host-key verification can expose credentials to an impostor host on a hostile network.

Mitigation: Require SSH host-key verification before password-based probes and prefer SSH keys over passwords.

Risk: Broad automatic triggers or writable command probes could cause unwanted activity.

Mitigation: Keep command probes read-only and narrow automatic routing triggers where supported.

Risk: Credentials stored directly in device configuration may be disclosed.

Mitigation: Keep real passwords and tokens out of devices.yaml; use SSH keys or credential environment variables.

## Reference(s):

- [Hearth on ClawHub](https://clawhub.ai/nj070574-gif/skills/hearth)
- [Installation guide](docs/INSTALL.md)
- [Configuration reference](docs/CONFIG.md)
- [Probe reference](docs/PROBES.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown health summary or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-device OK, DEGRADED, or DOWN status; sweep exit codes 0, 1, or 2.]

## Skill Version(s):

0.2.0 (source: server-resolved release and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
