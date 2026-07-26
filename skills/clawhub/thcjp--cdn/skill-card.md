## Description: <br>
Configure, optimize, and troubleshoot CDN deployments with caching strategies and security hardening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to plan, configure, optimize, and troubleshoot CDN deployments, including cache rules, security controls, performance tuning, and incident diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell execution and CDN API examples could affect production traffic or security controls if followed without review. <br>
Mitigation: Use scoped CDN tokens, prefer read-only diagnostics by default, and require explicit approval before cache purges, DNS/CDN configuration changes, WAF changes, or other live-traffic operations. <br>
Risk: Incorrect cache, WAF, DNS, or purge guidance can cause outages, stale content, or security exposure. <br>
Mitigation: Review proposed changes against provider documentation and test in a staging or limited-scope environment before applying them broadly. <br>


## Reference(s): <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CDN diagnostic reports, cache and security configuration summaries, and remediation guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
