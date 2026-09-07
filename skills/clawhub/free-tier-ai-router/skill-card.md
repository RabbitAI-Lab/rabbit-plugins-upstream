## Description:

Quota-aware LLM router that uses configured free-tier and OpenAI-compatible providers to route agent requests by measured availability, quality, and rate-limit state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose among free-tier and OpenAI-compatible LLM providers for repeated calls while avoiding exhausted quotas and tracking provider cooldowns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider credentials or custom endpoints may be used in ways the operator did not intend.

Mitigation: Review credential paths and providers.json before use, allow only expected endpoints, and avoid passing API keys as command-line arguments.

Risk: Probe, quality, and rate-limit utilities may expose keys in process arguments on shared machines.

Mitigation: Avoid running probe.py, quality.py, or ratelimit.py on shared machines until that behavior is fixed, or run them only in an isolated environment with disposable credentials.

Risk: Installation or repair behavior may make local configuration or cache changes that are not obvious to the operator.

Mitigation: Inspect install.sh, integrate.sh, and configured write paths before installation; test with a throwaway HOME when reviewing the release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Measurements](references/measurements.md)
- [Pluggable providers](references/providers.md)
- [Audit history](references/history.md)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Gemini API keys](https://aistudio.google.com/apikey)
- [OpenRouter keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown guidance, optional schema-versioned JSON, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON outputs are described by the bundled answer, status, plan, learn, and providers configuration schemas.]

## Skill Version(s):

2.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
