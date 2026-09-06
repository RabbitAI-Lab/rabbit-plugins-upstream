## Description:

free-tier-ai-router is a quota-aware LLM router that selects among configured free-tier and OpenAI-compatible model providers by measured quality, rate limits, cooldowns, and task needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route frequent LLM requests across configured free-tier or OpenAI-compatible providers while avoiding known quota and cooldown failures. It is intended for choosing routes, checking provider status, generating machine-readable plans, and setting up local router configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The router reads local LLM API keys and sends prompts to configured remote providers.

Mitigation: Install only from a trusted publisher, review configured provider endpoints, and avoid sending sensitive prompts unless the selected provider is acceptable.

Risk: Bootstrap paths such as get-ai-router.sh or mutable clawhub@latest installs may execute code that should be verified first.

Mitigation: Prefer pinned or checksum-verified artifacts and inspect installer scripts before execution.

Risk: Authenticated custom providers over plain HTTP can expose credentials or prompts outside the local machine.

Mitigation: Use HTTPS for authenticated providers and reserve unauthenticated HTTP for loopback-only local servers.

Risk: Benchmark and probe scripts can exercise real API keys on shared or monitored machines.

Mitigation: Run probes only in an appropriate environment and rotate affected keys afterward when exposure is possible.

Risk: Integration may restore credentials from ~/cred_backup into active configuration paths.

Mitigation: Review backup contents before running integration and remove stale credentials that should not be reactivated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Measurements](references/measurements.md)
- [Provider configuration guide](references/providers.md)
- [Audit history](references/history.md)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Gemini API keys](https://aistudio.google.com/apikey)
- [OpenRouter API keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON status or plan objects, and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit schema-versioned JSON for ask, status, plan, and learn modes; streaming and JSON output are mutually exclusive.]

## Skill Version(s):

2.4.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
