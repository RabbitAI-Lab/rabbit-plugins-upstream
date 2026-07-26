## Description: <br>
High-performance temporary storage system using Redis. Supports namespaced keys (mema:*), TTL management, and session context caching. Use for: (1) Saving agent state, (2) Caching API results, (3) Sharing data between sub-agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xiiang0529](https://clawhub.ai/user/xiiang0529) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to configure and operate a Redis-backed memory cache for temporary state, API result caching, and shared namespaced data across agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Redis cache data can expose agent state, private prompts, tokens, or customer data if the Redis service is reachable by untrusted parties or stores sensitive values. <br>
Mitigation: Use an approved Redis instance with authentication, TLS, restricted network access, and avoid caching secrets, tokens, private prompts, or sensitive customer data. <br>
Risk: Cached values can persist longer than intended when TTLs are omitted or set too broadly. <br>
Mitigation: Set reasonable TTLs for temporary context and cached API data, and reserve persistent keys for data that is approved to remain in Redis. <br>
Risk: Unpinned Python dependencies may change behavior across installs. <br>
Mitigation: Pin or regularly update and review the Redis and python-dotenv dependencies before production use. <br>


## Reference(s): <br>
- [Redis Key Naming Standards](references/key-standards.md) <br>
- [Memory Cache ClawHub Release](https://clawhub.ai/xiiang0529/skills/memory-cache) <br>
- [xiiang0529 ClawHub Profile](https://clawhub.ai/user/xiiang0529) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and plain-text Redis command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Redis keys in the mema: namespace and optional TTL values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
