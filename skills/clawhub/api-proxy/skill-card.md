## Description:

API Gateway is a local proxy for external API calls with retry handling, metadata-only caching by default, rate-limit tracking, circuit breaking, fallback providers, and disclosed key-storage controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jlacroix82](https://clawhub.ai/user/jlacroix82)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to centralize outbound API calls through one local gateway with retries, caching controls, rate-limit awareness, fallback routing, and masked API-key management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outbound calls send request URLs, headers, bodies, prompts, and responses to the provider endpoint selected by the user.

Mitigation: Install only when a local API gateway is desired, call only trusted endpoints, and use provider allowlists carefully.

Risk: API keys stored with the skill are plaintext on disk, even with chmod 0600 permissions.

Mitigation: Prefer environment variables or a secrets manager for sensitive keys, especially in shared, production, or CI environments.

Risk: Full-body caching can write complete provider responses to disk when explicitly enabled.

Mitigation: Avoid --cache-full for sensitive responses and clear logs or cache after sensitive work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local gateway commands and configuration guidance; runtime calls may create JSON data files under memory/api-gateway.]

## Skill Version(s):

1.1.11 (source: server release evidence and artifact clawhub.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
