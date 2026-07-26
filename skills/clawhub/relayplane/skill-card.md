## Description: <br>
RelayPlane is an OpenClaw agent-operations layer for LLM routing, observability, governance, cost optimization, and automatic failover. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[relayplane](https://clawhub.ai/user/relayplane) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use RelayPlane to route LLM requests through a local proxy, monitor usage, enforce budgets and policies, and fall back to direct provider calls when the proxy is unhealthy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conflicting setup paths can route more LLM API traffic through RelayPlane than intended, especially when global BASE_URL variables are used. <br>
Mitigation: Prefer the OpenClaw relayplane configuration with circuit breaker, avoid global BASE_URL variables unless intentionally routing all traffic, and confirm how to stop the background proxy. <br>
Risk: Installing external npm packages and running a local LLM proxy changes request routing, telemetry, and logging behavior. <br>
Mitigation: Pin and verify the external npm packages before use, review telemetry, logging, and offline settings, and use offline mode where needed. <br>


## Reference(s): <br>
- [ClawHub RelayPlane skill listing](https://clawhub.ai/relayplane/skills/relayplane) <br>
- [RelayPlane documentation](https://relayplane.com/docs) <br>
- [RelayPlane npm package](https://www.npmjs.com/package/@relayplane/proxy) <br>
- [RelayPlane homepage](https://relayplane.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and TypeScript snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only OpenClaw skill; model invocation is disabled.] <br>

## Skill Version(s): <br>
4.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
