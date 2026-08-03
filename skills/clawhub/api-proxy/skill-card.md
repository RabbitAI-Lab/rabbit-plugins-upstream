## Description: <br>
api-gateway is a local smart proxy for external API calls with retry, caching, rate limiting, fallback providers, and API key management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route outbound HTTPS API calls through a local gateway that centralizes retries, rate-limit handling, caching, circuit breaking, fallback providers, and API key handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local key and cache files can persist sensitive data, including plaintext API keys and cache keys derived from endpoint paths and request bodies; full-body caching can also persist complete provider responses. <br>
Mitigation: Prefer provider API keys from environment variables or a secrets manager, avoid routing regulated or proprietary prompts through the gateway, avoid full-body caching for sensitive providers, and clear cache and log files after sensitive work. <br>
Risk: Outbound calls transmit prompts, request bodies, headers, and responses to third-party API providers. <br>
Mitigation: Use allowlisted provider domains, run dry runs before important calls, and only send data that is approved for the target provider. <br>
Risk: The ClawHub security verdict is suspicious because the default cache behavior may retain more sensitive request metadata than the documentation suggests. <br>
Mitigation: Treat local cache files as sensitive, review cache contents and retention before deployment, and disable or regularly clear caching where request bodies or endpoint paths may contain secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-like API responses or status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes local API key, cache, request log, rate-limit, circuit-breaker, and fallback state files under memory/api-gateway/ unless configured otherwise.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release metadata and artifact/clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
