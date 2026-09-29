## Description: <br>
Configures, optimizes, and troubleshoots CDN deployments, including caching strategies, security hardening, performance tuning, and operational diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and site reliability teams use this skill to plan CDN domain onboarding, cache behavior, security controls, performance tuning, and troubleshooting steps for web delivery operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is intended for CDN operations and asks for broad command, API, and file authority that can affect infrastructure. <br>
Mitigation: Review proposed actions before installation and require explicit confirmation before cache purges, configuration changes, file writes, or authenticated requests. <br>
Risk: Provider API examples and API key setup can involve credentials and authenticated CDN changes. <br>
Mitigation: Use scoped credentials, keep secrets out of version control, and verify the target domain, zone, and action before executing provider API commands. <br>
Risk: CDN cache and security guidance can cause stale content, origin overload, blocked legitimate traffic, or sensitive data exposure if applied incorrectly. <br>
Mitigation: Test changes in a controlled environment, review cache rules and WAF behavior, and roll out high-impact updates gradually with monitoring. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CDN configuration recommendations, diagnostics, provider API command examples, and operational checklists.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
