## Description: <br>
Proxy Aiops helps agents inspect, analyze, and safely operate Traefik, Caddy, and HAProxy reverse proxies, including routes, upstream health, certificates, 5xx RCA, audited writes, and undo workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and SRE teams use this skill to observe reverse-proxy state, troubleshoot 502/503/504 errors, investigate backend health and certificate expiry, and make governed Caddy or HAProxy changes with audit and undo support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make outage-causing reverse-proxy changes while relying on external account permissions and agent judgment rather than an internal read-only control. <br>
Mitigation: Start with read-only or tightly scoped proxy credentials where possible, keep admin APIs private, and require explicit workflow approval for Caddy config loads/deletes and HAProxy drain or weight changes. <br>
Risk: Plaintext legacy proxy secret environment variables may expose credentials. <br>
Mitigation: Use the encrypted secrets store and avoid plaintext PROXY_<TARGET>_SECRET variables. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/AIops-tools/Proxy-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell commands and structured operational findings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute read and governed write workflows through proxy-aiops tools, depending on the connected agent and operator permissions.] <br>

## Skill Version(s): <br>
0.5.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
