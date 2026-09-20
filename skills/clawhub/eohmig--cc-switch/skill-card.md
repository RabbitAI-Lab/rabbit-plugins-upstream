## Description:

Manage API providers for Codex and compatible CLI tools with automatic mode detection, pre-switch connectivity tests, and endpoint URL updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add, list, test, delete, and switch API providers for local agent CLI workflows. It is most useful when managing Claude-compatible provider endpoints across cc-switch SQLite state or standalone JSON configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer and documentation support remote download and curl-to-bash style installation.

Mitigation: Review the installer and scripts locally before installation, and prefer a manual install path over piping remote content directly to a shell.

Risk: Provider API keys are stored in local SQLite or JSON configuration and should be treated as plaintext secrets.

Mitigation: Use restrictive file permissions, avoid sharing configuration files, and rotate provider keys if local storage is exposed.

Risk: Connectivity tests send requests to configured provider endpoints and may expose credentials to an unintended URL if the provider is misconfigured.

Mitigation: Verify each provider base URL before testing or switching, especially for custom providers.

Risk: Switching providers persistently changes local provider state or agent settings.

Mitigation: List current providers and back up relevant settings before switching, then confirm the active endpoint after the operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/eohmig/skills/cc-switch)
- [Publisher profile](https://clawhub.ai/user/eohmig)
- [Skill instructions](artifact/SKILL.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run local shell scripts that read or update provider state, test network connectivity, and modify local agent settings.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
