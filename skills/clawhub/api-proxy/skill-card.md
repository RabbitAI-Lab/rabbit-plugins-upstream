## Description: <br>
API Gateway is a local Node.js API proxy that helps agents make external API calls with retry, metadata-only caching, rate-limit tracking, circuit breaking, fallback providers, and API key management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route API calls through a reusable gateway with retries, caching, circuit breaking, fallback providers, and API key handling. It is intended for workflows that need controlled outbound provider calls and local visibility into request, cache, rate-limit, and key state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Environment-sourced PROVIDER_API_KEY credentials can be attached to any supplied endpoint despite the documented provider allowlist boundary. <br>
Mitigation: Avoid exposing provider API key environment variables to this skill until environment-sourced keys enforce the same allowlist and HTTPS-only checks; use dry-run and narrow disk-key allowlists for sensitive providers. <br>
Risk: API keys saved through the skill are persisted as plaintext in keys.json, even though file permissions are set to 0600 where supported. <br>
Mitigation: Use least-privileged keys, limit workspace access, remove stored keys when no longer needed, and prefer an external secrets manager for production use. <br>
Risk: Outbound requests, cache entries, and request logs may expose sensitive workflow context if arbitrary endpoints or regulated data are used. <br>
Mitigation: Keep provider allowlists narrow, avoid routing secrets or regulated data through arbitrary endpoints, keep full-body caching disabled unless required, and clear cache and logs after sensitive work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill source instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples; CLI calls return text or JSON-like API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses outbound HTTP(S), local state files, metadata-only response caching by default, and opt-in full-body caching per provider.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
