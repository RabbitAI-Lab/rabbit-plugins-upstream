## Description:

API Gateway is a local Node.js proxy for outbound API calls with retry, caching, rate-limit handling, circuit breaking, key management, and fallback providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route external API calls through a single gateway that handles retries, caching, rate limits, circuit breaker state, API keys, and provider fallback behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request bodies can be persisted locally in the default cache key, despite metadata-only cache disclosure.

Mitigation: Avoid sensitive request bodies, clear cache after use, and update the cache-key implementation to hash request bodies instead of storing them.

Risk: API keys may be stored as plaintext on disk.

Mitigation: Prefer PROVIDER_API_KEY environment variables where possible, restrict workspace access, and use a secrets manager for production deployments.

Risk: Prompts, request bodies, headers, and responses are sent to user-selected third-party API providers.

Mitigation: Use only trusted provider endpoints, review provider data-retention terms, and run dry runs before important calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy)
- [README.md](README.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-line text with JSON-compatible status and API response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local key, cache, log, rate-limit, circuit-breaker, and fallback state files under memory/api-gateway.]

## Skill Version(s):

1.1.9 (source: server release metadata and artifact/clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
