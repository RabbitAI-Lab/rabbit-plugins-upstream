## Description:

Agent Credential Vault - Anima helps agents authenticate and call APIs through Anima's credential vault without exposing passwords, API keys, or TOTP codes to the model context, argv, logs, or traces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diyanbogdanov](https://clawhub.ai/user/diyanbogdanov)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to provision and use Anima Vault credentials for agents that need to log in or call APIs while keeping secrets out of prompts, command arguments, logs, traces, and broad process environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on Anima as a third-party credential broker for sensitive credential handling.

Mitigation: Install only when that broker relationship is acceptable, and prefer owner approval, brokered reveal policies, and allowed-host restrictions.

Risk: Secrets resolved into subprocess environments may be exposed by downstream tools, logs, or transcripts.

Mitigation: Use dry-runs before execution and apply vault redaction or audit commands before storing or sharing transcripts and files.

Risk: A credential could be misused against unintended hosts if host restrictions are omitted.

Mitigation: Set repeatable allowed-host restrictions for API-key credentials and use brokered reveal policies so credentials are not returned as plaintext.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diyanbogdanov/skills/agent-credential-vault)
- [Anima homepage](https://useanima.sh)
- [Anima documentation](https://docs.useanima.sh)
- [Anima API base](https://api.useanima.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential-vault command examples, brokered reveal-policy guidance, allowed-host restrictions, dry-run usage, redaction, and audit guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
