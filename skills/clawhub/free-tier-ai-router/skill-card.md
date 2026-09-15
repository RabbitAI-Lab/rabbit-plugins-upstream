## Description:

Free Tier AI Router routes agent LLM requests across free-tier and OpenAI-compatible providers by measuring quality, rate limits, cooldowns, and local state so agents can avoid avoidable quota failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to route high-volume LLM calls across free-tier provider keys, local OpenAI-compatible endpoints, and fallback providers while conserving scarce quota. It is most useful when an agent needs many model calls without repeated rate-limit failures or needs a machine-readable plan, status, or answer contract.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer and credential-handling paths can expose API keys.

Mitigation: Review before installing, use the normal package path, and do not pass API keys on the command line.

Risk: Probe, quality, and rate-limit scripts can use real provider keys on machines where process, shell, or network activity may be monitored.

Mitigation: Avoid running probe.py, quality.py, or ratelimit.py with real keys on shared or monitored machines.

Risk: Custom provider configuration can create unsafe unauthenticated or non-HTTPS network paths.

Mitigation: Restrict custom providers to HTTPS endpoints or true loopback HTTP endpoints.

Risk: Credential backup behavior can reactivate saved credentials unexpectedly.

Mitigation: Check ~/cred_backup before running integrate.sh.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Measurements](artifact/references/measurements.md)
- [Provider configuration guide](artifact/references/providers.md)
- [Model capability tags](artifact/references/model-tags.md)
- [Audit history](artifact/references/history.md)
- [Machine contract schemas](artifact/schema/)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Gemini API keys](https://aistudio.google.com/apikey)
- [OpenRouter keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON]

**Output Format:** [Plain text, Markdown, shell commands, configuration snippets, and schema-versioned JSON objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit answer, status, plan, and learn JSON contracts; streaming output is available for OpenAI-compatible transports.]

## Skill Version(s):

2.5.4 (source: server release evidence; artifact frontmatter reports 2.5.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
