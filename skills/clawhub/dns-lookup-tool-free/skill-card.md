## Description: <br>
DNS查询免费版帮助运维与开发者使用 dig 查询 A、AAAA、CNAME、MX、TXT、NS、SOA 和 PTR 记录，并将结果整理为可读的 DNS 诊断输出。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
运维人员和开发者可用它排查域名解析、DNS 变更、邮件记录、CDN CNAME 链和 IPv6 支持等问题。涉及内部域名或敏感基础设施时，应使用可信内部解析器。 <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DNS lookups against public resolvers can expose private internal hostnames, incident indicators, or sensitive infrastructure names. <br>
Mitigation: Use the skill only for explicit DNS troubleshooting and route sensitive lookups through a trusted internal resolver. <br>
Risk: The skill runs shell DNS queries and depends on local dig availability and network reachability. <br>
Mitigation: Review proposed commands before execution and confirm dig, resolver choice, and network access match the troubleshooting task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns-lookup-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured diagnostic output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the local dig command and network access to DNS resolvers; no API key is required.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
