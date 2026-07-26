## Description: <br>
DNS配置工具免费版 helps personal developers and small sites prepare DNS migrations, tune TTL values, configure SPF/DKIM/DMARC records, handle apex and www domains, and run basic DNS validation commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and site operators use this skill for DNS configuration guidance on personal blogs, project sites, and small business email authentication. It produces TTL migration steps, SPF/DKIM/DMARC record guidance, apex/www handling advice, and command-line checks for DNS propagation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security verdict is suspicious because the skill requests broad agent tools and contains overbroad or inconsistent instructions. <br>
Mitigation: Keep invocation limited to DNS tasks and review suggested actions before execution. <br>
Risk: Incorrect DNS changes can interrupt site availability or email delivery. <br>
Mitigation: Back up current DNS records, review changes manually in the DNS provider dashboard, and require explicit confirmation before changing TTL, A/AAAA, MX, TXT, SPF, DKIM, or DMARC records. <br>
Risk: The artifact includes unrelated messaging/API limitation text that may confuse users about the skill's scope. <br>
Mitigation: Treat DNS guidance as the supported scope and have the publisher clean up unrelated limitation text before broader deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/dns-config-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with DNS record examples, bash commands, and structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may suggest DNS record changes, TTL values, validation commands, and manual checks in a DNS provider dashboard.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
