## Description: <br>
Smart proxy for external API calls with retry, caching, rate limiting, and fallback providers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route outbound HTTPS API calls through a local gateway with retries, rate-limit handling, response caching, circuit breaking, fallback providers, and API-key management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The gateway can send request bodies, prompts, headers, and responses to third-party API providers. <br>
Mitigation: Route only to trusted provider endpoints, use dry runs for important calls, and avoid sending sensitive or regulated data through the gateway. <br>
Risk: API keys and gateway state may be stored in local files, including plaintext keys in memory/api-gateway/keys.json. <br>
Mitigation: Prefer PROVIDER_API_KEY environment variables, restrict workspace access, and treat memory/api-gateway/keys.json and cache files as sensitive. <br>
Risk: Full-body caching can persist complete API responses to disk when enabled. <br>
Mitigation: Keep the default metadata-only cache for sensitive providers, avoid --cache-full for sensitive data, and clear cache and log files after sensitive work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jlacroix82/skills/api-proxy) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jlacroix82) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local gateway commands and configuration guidance; runtime calls may also create local JSON state files.] <br>

## Skill Version(s): <br>
1.1.8 (source: server release evidence and artifact clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
