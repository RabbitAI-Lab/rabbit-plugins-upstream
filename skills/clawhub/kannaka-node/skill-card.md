## Description:

Helps an agent provision a fresh Linux server into a running Kannaka node over SSH, including preflight checks, installation, configuration, systemd service setup, verification, and hand-off reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickflach](https://clawhub.ai/user/nickflach)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they have SSH access to a new VPS or cloud instance and want an agent to provision it as a Kannaka node. The skill is especially oriented toward Oracle Cloud free-tier hosts, while also covering Ubuntu, Debian, Fedora, and similar Linux servers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary says the skill installs a mutable remote script into persistent services.

Mitigation: Review before installing on important hosts, use only disposable or freshly provisioned servers, and keep INSTALL_URL set to a trusted value.

Risk: The server security summary flags unsafe shell interpolation risks.

Mitigation: Avoid untrusted environment and configuration values, especially values used in generated shell or systemd content, and review the generated changes before relying on the node.

Risk: Swarm credentials and SSH access are sensitive operational inputs.

Mitigation: Provide credentials only through the documented environment variables or an already loaded SSH agent, and avoid logging or embedding secrets in commands, files, or hand-off text.

## Reference(s):

- [Oracle Cloud free tier, for a Kannaka node](references/oracle-cloud.md)
- [Things that have actually gone wrong on real Kannaka nodes](references/traps.md)
- [ClawHub skill page](https://clawhub.ai/nickflach/skills/kannaka-node)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and hand-off report text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause the agent to create remote configuration files, systemd units, credential environment files, and service reports on the target server.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
