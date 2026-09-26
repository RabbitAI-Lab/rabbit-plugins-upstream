## Description: <br>
This skill helps agents manage Volcengine DNS records, including zone record queries and DNS record updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, infrastructure operators, and automation agents use this skill to query and change DNS records for Volcengine-hosted networking services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent toward DNS create, update, or delete operations that can affect infrastructure availability. <br>
Mitigation: Use tightly scoped credentials and require explicit human confirmation before DNS-changing operations. <br>
Risk: The skill documentation references broad command authority and an unclear credential boundary. <br>
Mitigation: Avoid broad shell access or generic API keys; provide only zone-specific or task-specific credentials. <br>
Risk: The security scan classified the release as suspicious because operational safeguards are weakly specified. <br>
Mitigation: Review the skill before installation and verify domain, zone, and record identifiers before executing generated guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/volcengine-network-dns) <br>
- [Volcengine DNS API endpoint](https://api.volcengine.com/dns/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe DNS query or update results, API request examples, required environment variables, and operational guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
