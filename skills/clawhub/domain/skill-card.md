## Description: <br>
Check domain availability, search domains by keyword across newly registered, expired, deleted, active, and marketplace datasets, and analyze keyword value and domain trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abtdomain](https://clawhub.ai/user/abtdomain) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, domain operators, marketers, and naming teams use this skill to find available domains, inspect WHOIS and DNS records, compare pricing, monitor changes, and turn domain search results into actionable recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Domain searches, keywords, and optional API keys are sent to the remote DomainKits MCP service. <br>
Mitigation: Use an API key only when needed, avoid submitting sensitive domain strategy data unless appropriate, and review DomainKits account and privacy settings before use. <br>
Risk: Memory-backed preferences, monitors, and strategies can store domain-related data with DomainKits when enabled. <br>
Mitigation: Keep memory off unless storage is intended, obtain consent before saving data, and use the preferences delete action when stored data should be removed. <br>
Risk: Some tools are account-gated or quota-limited, which can affect completeness of safety, keyword, backlink, trend, bulk, and monitoring workflows. <br>
Mitigation: Check remaining quota with the usage tool before heavy operations and disclose when results are limited by access tier. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/abtdomain/skills/domain) <br>
- [DomainKits MCP](https://domainkits.com/mcp) <br>
- [DomainKits Pricing](https://domainkits.com/pricing) <br>
- [DomainKits Registration](https://domainkits.com/register) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with domain data summaries, verdicts, setup commands, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include availability status, pricing, WHOIS/RDAP, DNS, safety, keyword, trend, marketplace, monitoring, and quota information depending on the selected DomainKits tool and account tier.] <br>

## Skill Version(s): <br>
3.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
