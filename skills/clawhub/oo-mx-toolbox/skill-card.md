## Description:

MxToolbox helps an agent run live DNS, blacklist, mail-record, monitor-status, and usage lookups through an OOMOL-connected MxToolbox account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and support agents use this skill to inspect DNS, mail authentication, blacklist, SMTP, HTTP, ping, monitor, and API usage data for domains or IP addresses through MxToolbox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account-level actions can expose monitor status and API usage for the connected MxToolbox account.

Mitigation: Use account-level actions only when the user asks for that account information, and avoid sharing returned monitor or usage details outside the intended task.

Risk: Live domain and IP lookups may disclose the queried targets to the connected MxToolbox service and can consume account usage or credits.

Mitigation: Confirm sensitive targets before lookup when appropriate, and stop on billing or insufficient-credit errors until the user resolves the account state.

Risk: First-time setup may require installing the oo CLI and signing in to OOMOL.

Mitigation: Run setup steps only after an auth, connection, or missing-CLI failure, and do not proactively start login or connection flows.

## Reference(s):

- [MxToolbox homepage](https://mxtoolbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mx-toolbox)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
