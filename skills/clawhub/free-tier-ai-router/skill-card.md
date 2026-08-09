## Description:

Quota-aware LLM router for agents that use free-tier API keys across Gemini, Mistral, OpenRouter, Kilo, and Cerebras while tracking measured quality, rate limits, cooldowns, cache state, and provider availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route repeated LLM calls across available free-tier provider keys, choose models by task and measured quality, and reduce avoidable 429s or quota waste. It is intended for environments where local credential files and outbound calls to third-party LLM APIs are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The router reads local provider API keys and sends prompts to third-party LLM APIs.

Mitigation: Install only in environments where those providers are approved, avoid sensitive prompts unless provider terms allow them, and keep credential files limited to the intended user account.

Risk: Installer and integration scripts can alter credential state and local router entry points.

Mitigation: Review the scripts before running them, back up credentials first, and confirm changes to files such as ~/.config/*/credentials.json, ~/.cache/ai_router/state.json, and ~/ai.

Risk: Probe and rate-limit scripts can spend provider quota through broad credential-backed calls.

Mitigation: Run probing or rate-limit measurement only when quota consumption is expected, and prefer status or plan modes when checking routing behavior without calls.

Risk: Passing API keys on command lines can expose credentials on shared systems.

Mitigation: Avoid command-line key arguments on shared hosts and use reviewed credential files or interactive setup flows where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Google AI Studio API key](https://aistudio.google.com/apikey)
- [OpenRouter keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)
- [Gemini API endpoint](https://generativelanguage.googleapis.com)
- [Mistral API endpoint](https://api.mistral.ai)
- [OpenRouter API endpoint](https://openrouter.ai)
- [Kilo API endpoint](https://api.kilo.ai)
- [Cerebras API endpoint](https://api.cerebras.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, configuration paths, and generated command-line responses from the router]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call third-party LLM APIs, read provider credential files, write router state/cache under the user's home directory, and emit status, plans, setup diagnostics, or routed model responses.]

## Skill Version(s):

2.2.8 (source: server release evidence; artifact frontmatter says 2.1.0 and artifact _meta.json says 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
