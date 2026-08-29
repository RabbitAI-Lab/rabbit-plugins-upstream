## Description:

Free Tier AI Router routes LLM requests across configured free-tier and OpenAI-compatible providers using measured quality, rate limits, cooldowns, and cache state to conserve quota.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose among multiple configured LLM provider keys, avoid known rate limits, and keep requests working when individual providers or models are exhausted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local LLM API keys and send prompts to configured external providers.

Mitigation: Install only with provider accounts and prompt data you are comfortable routing through those APIs, and review credential files before use.

Risk: The router can spend provider quota and broad probe helpers can trigger live API testing.

Mitigation: Use normal routing commands for day-to-day work and run probe, quality, or ratelimit helpers only when broad live testing is intended.

Risk: Integration can write under ~/.config and ~/.cache/ai_router and create or overwrite ~/ai.

Mitigation: Review ~/cred_backup, providers.json, and the existing ~/ai entry point before running integrate.sh.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router)
- [Mistral API keys](https://console.mistral.ai/api-keys)
- [Gemini API keys](https://aistudio.google.com/apikey)
- [OpenRouter keys](https://openrouter.ai/keys)
- [Kilo profile](https://app.kilo.ai/profile)

## Skill Output:

**Output Type(s):** [Text, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, Markdown, command-line output, or JSON depending on router options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send prompts to configured providers, consume provider quota, persist cooldown and cache state, and update local configuration files.]

## Skill Version(s):

2.2.9 (source: server release metadata; artifact frontmatter reports 2.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
