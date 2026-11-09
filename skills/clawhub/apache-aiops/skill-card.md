## Description:

Helps users inspect and diagnose Apache HTTP Server configuration, virtual hosts, modules, status, and logs, and perform a guarded graceful reload; it requires local apachectl access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and system administrators use the skill to inspect Apache configuration, virtual hosts, modules, HTTP status, and selected logs while diagnosing service issues. They can request a guarded graceful reload after checking configuration syntax.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A graceful reload can change the running Apache service, and its final state may remain unknown while existing workers use old configuration.

Mitigation: Use the dry run and config check first, require the documented confirmations, then inspect service status and traffic before retrying.

Risk: Configured Apache logs, status endpoints, and configuration may expose operational information to the process account.

Mitigation: Select only trusted local files and a restricted status endpoint, avoid URLs containing credentials, and grant the process account only the access needed for the chosen checks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/apache-aiops)
- [Project homepage](https://github.com/AIops-tools/Apache-AIops)
- [Agent guardrails](artifact/references/agent-guardrails.md)
- [Capabilities](artifact/references/capabilities.md)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Structured diagnostic results and concise guidance; CLI commands as shell text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Access summaries contain HTTP status codes without raw URLs, IP addresses, or headers. Results distinguish failed probes from completed but unhealthy checks; reload status may remain unknown until the target is checked.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
