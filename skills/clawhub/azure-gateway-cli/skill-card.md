## Description: <br>
Guides agents through configuring and operating a local Azure OpenAI gateway with multi-endpoint routing, load balancing, failover, request caching, cost tracking, tenant isolation, and optional service setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to configure a local gateway for shared Azure OpenAI access, endpoint failover, request caching, tenant-level key management, and cost governance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide setup of a local Azure OpenAI gateway that handles API keys and tenant configuration. <br>
Mitigation: Keep keys in environment variables or a secret store, avoid committing credential-bearing configuration, and review tenant-level key handling before use. <br>
Risk: Request and response caching may store sensitive prompt or output data. <br>
Mitigation: Disable caching for sensitive workloads unless cache storage, retention, and exclusion behavior are understood and acceptable. <br>
Risk: Local operational endpoints and optional background services may expose gateway state or continue running after setup. <br>
Mitigation: Keep the gateway bound to localhost unless protected by access controls, and review service commands before enabling automatic startup. <br>
Risk: The provided documentation is inconsistent and references missing scripts or commands. <br>
Mitigation: Verify actual executable files and commands before running them, and do not substitute untrusted scripts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-gateway-cli) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline YAML, JSON, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes configuration examples, local endpoint checks, and optional service setup guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
