## Description:

Smart proxy for external API calls with retry, caching, rate limiting, and fallback providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route outbound HTTPS API requests through a local gateway with retry, metadata caching, rate-limit tracking, circuit breaking, fallback providers, and masked API-key handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Request bodies, prompts, headers, and responses are sent to the API provider endpoint selected by the user.

Mitigation: Use only trusted provider endpoints, configure strict allowlist domains, and avoid routing sensitive or regulated data unless the provider and use case are approved.

Risk: API keys saved through the gateway are stored locally in plaintext, even though the file is created with owner-only permissions where supported.

Mitigation: Prefer PROVIDER_API_KEY environment variables or a secrets manager for valuable keys, and remove stored keys when they are no longer needed.

Risk: Full response bodies can be written to the local cache when full-body caching is enabled.

Mitigation: Keep the default metadata-only cache for sensitive providers, avoid --cache-full for sensitive work, and clear cache and logs after sensitive sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger outbound HTTPS requests to configured provider endpoints and may write local gateway state under memory/api-gateway/.]

## Skill Version(s):

1.1.9 (source: server release metadata and artifact/clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
