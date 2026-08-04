## Description: <br>
Smart proxy for external API calls with retry, caching, rate limiting, fallback providers, strict provider-domain allowlists, and disclosed local persistence of keys and request/cache metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use api-gateway to route outbound HTTPS API calls through a local Node.js gateway that centralizes retries, rate-limit handling, caching, key lookup, and provider fallback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The gateway handles API keys and may store them as plaintext local state. <br>
Mitigation: Prefer PROVIDER_API_KEY environment variables or a secrets manager, restrict workspace access, and review stored key files before use. <br>
Risk: User-specified requests, prompts, headers, and bodies are sent to third-party API providers. <br>
Mitigation: Configure provider allowlists carefully, use dry runs for important calls, and send data only to trusted endpoints. <br>
Risk: Cache and log files can persist request/cache data, especially when full response caching is enabled. <br>
Mitigation: Keep the default metadata-only cache for sensitive providers, avoid --cache-full for sensitive work, and clear cache/log files after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local gateway usage guidance and commands; actual API responses depend on user-configured providers.] <br>

## Skill Version(s): <br>
1.1.7 (source: server release metadata and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
