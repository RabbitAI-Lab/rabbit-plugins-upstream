## Description:

Let agents log in and call APIs through Anima Vault while credentials remain encrypted at rest and brokered outside the model context, argv, logs, and traces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anima](https://clawhub.ai/user/anima)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to provision Anima Vault credentials for agents, broker authenticated API calls, inject secrets into subprocesses, and audit or redact credential material without exposing raw secrets by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw credential reveal commands such as vault get or vault totp can expose secrets in terminal history, logs, traces, or agent context.

Mitigation: Prefer brokered reveal policies and use raw reveal commands only when a human intentionally needs the value.

Risk: Credential use without host limits could allow secrets to be sent to unintended destinations.

Mitigation: Set allowed-host restrictions for brokered API credentials and review host scope before agent use.

Risk: Executing subprocesses with resolved secrets may disclose sensitive values if the command behaves unexpectedly.

Mitigation: Run vault exec with dry-run first and inspect which references will resolve before executing commands.

## Reference(s):

- [Anima homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima API base](https://api.useanima.sh)
- [ClawHub skill page](https://clawhub.ai/anima/skills/agent-credential-vault)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential provisioning, storage, brokered use, subprocess injection, reveal, audit, and redaction workflows.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
