## Description:

Switch opencode between buying from the asale market and using its own subscription, and show which running sessions are still using the old configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and opencode users use this skill to configure opencode to route new sessions through the local asale daemon, choose market models, restore the original configuration, and identify running sessions that still need to be restarted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions execute remote scripts directly in a shell without pinning or checksum verification.

Mitigation: Review the installer source before installing and prefer a pinned, signed, or checksum-verified release when available.

Risk: Runtime use reads the local asale daemon token and sends authenticated requests to the local daemon.

Mitigation: Keep the daemon token private, use the loopback daemon endpoint only, and stop if authentication fails.

Risk: The skill modifies opencode configuration and reports running opencode processes.

Mitigation: Review configuration changes before relying on them, restart affected sessions manually, and do not stop reported processes from the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/asale-buy-opencode)
- [asale homepage](https://asale.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is centered on local daemon RPC calls, opencode configuration changes, model selection, and process-status reporting.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
