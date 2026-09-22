## Description:

Free Ride helps OpenClaw agents configure free OpenRouter models, rank available free models, and set fallback model chains for rate-limit resilience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiiang0529](https://clawhub.ai/user/xiiang0529)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to reduce model costs by selecting free OpenRouter models, configuring ranked fallbacks, and recovering from rate-limit failures. It is intended for OpenClaw environments where the user opts into OpenRouter API access and model configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify OpenClaw model defaults, fallback models, and model allowlist settings.

Mitigation: Review the intended OpenClaw configuration changes, keep backups of important configuration, and restart the OpenClaw gateway only after confirming the selected models are acceptable.

Risk: The skill uses an OpenRouter API key to fetch and probe model availability.

Mitigation: Use an intended OpenRouter key, store it through environment or OpenClaw secret configuration, and rotate or revoke the key if it is exposed.

Risk: The optional watcher runs continuously and can automatically rotate model configuration.

Mitigation: Run the watcher only when continuous monitoring is desired, supervise it with the user's preferred process manager, and inspect its state or logs during troubleshooting.

Risk: Installer and Python dependency versions may change over time.

Mitigation: Use pinned installer and dependency versions in security-sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiiang0529/skills/free-ride)
- [Publisher profile](https://clawhub.ai/user/xiiang0529)
- [OpenRouter API keys](https://openrouter.ai/keys)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [OpenRouter models API](https://openrouter.ai/api/v1/models)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write OpenClaw model configuration and Free Ride cache or watcher state files when the recommended CLI commands are executed.]

## Skill Version(s):

1.0.0 (source: target metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
