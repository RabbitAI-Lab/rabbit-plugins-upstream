## Description:

Manages free AI models from OpenRouter for OpenClaw. Automatically ranks models by quality, configures fallbacks for rate-limit handling, and updates openclaw.json. Optional Groq, Gemini and Cerebras free tiers are opt-in. Use when the user mentions free AI, OpenRouter, model switching, rate limits, or wants to reduce AI costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shaivpidadi](https://clawhub.ai/user/shaivpidadi)

### License/Terms of Use:

MIT No Attribution

## Use Case:

OpenClaw users and developers use FreeRide to select free OpenRouter models, configure ranked fallbacks, and restore prior model settings. Optional provider tiers can be enabled explicitly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill changes local OpenClaw model settings and can run a persistent background watcher.

Mitigation: Review the proposed model changes and backup behavior; enable the watcher only when ongoing monitoring is wanted.

Risk: Model requests and credentials involve external AI providers, and the security scan is incomplete.

Mitigation: Review the enabled providers and their data terms, keep API keys in the local environment file, and inspect unresolved scan paths and the installed requests dependency before use.

## Reference(s):

- [FreeRide project homepage](https://github.com/Shaivpidadi/FreeRide)
- [FreeRide on ClawHub](https://clawhub.ai/shaivpidadi/skills/free-ride)
- [OpenRouter API overview](https://openrouter.ai/docs/api-reference/overview)
- [OpenClaw project](https://github.com/openclaw/openclaw)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Guidance]

**Output Format:** [OpenClaw model configuration (JSON), shell commands, and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates model and fallback settings; API keys are not written.]

## Skill Version(s):

1.1.0 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
