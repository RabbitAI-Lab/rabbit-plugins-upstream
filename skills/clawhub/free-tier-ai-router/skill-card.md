## Description:

Quota-aware LLM router that probes free-tier provider capacity and routes agent requests across Gemini, Mistral, OpenRouter, Kilo, and Cerebras while preserving scarce quota.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route high-volume LLM calls across free-tier provider keys, avoid known exhausted routes, and choose models by task, latency, quality, and available quota.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer, credential restoration, debug, and recovery helpers can modify local state beyond ordinary request routing.

Mitigation: Review the package before installation, run only the setup path you need, and avoid debug or recovery helpers unless their local process, filesystem, and package-management effects are acceptable.

Risk: Provider API keys and prompt content are handled by local scripts and forwarded to selected third-party AI providers.

Mitigation: Use only intended provider keys, keep credential files protected, avoid passing keys on the command line, and use --no-cache for sensitive prompts.

## Reference(s):

- [free-tier-ai-router ClawHub page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Google AI Studio API keys](https://aistudio.google.com/apikey)
- [OpenRouter keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and command-line guidance with executable shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce provider requests, local state updates, cache entries, diagnostics, and routing plans depending on the command used.]

## Skill Version(s):

2.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
