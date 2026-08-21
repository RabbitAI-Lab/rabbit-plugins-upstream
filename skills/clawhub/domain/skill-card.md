## Description:

Check domain availability, search domains by keyword across the domain lifecycle, analyze keyword value and trends, and help agents act on DomainKits domain intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abtdomain](https://clawhub.ai/user/abtdomain)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search domain availability, inspect DNS and WHOIS/RDAP data, evaluate pricing and market signals, monitor domain changes, and support domain naming or due-diligence workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Domain searches, lookups, and optional API keys are sent to DomainKits.

Mitigation: Review DomainKits terms and privacy posture before enabling the skill, and use guest access when an account-bound API key is not required.

Risk: Account-bound tools can manage monitors, preferences, strategy storage, keyword data, and backlink lookups.

Mitigation: Enable account-bound tools only for intended workflows, keep memory off unless explicitly needed, and delete stored preferences or data when no longer required.

Risk: Heavy or deeper operations can depend on the current quota and access tier.

Mitigation: Use the usage tool to check remaining quota before high-volume operations and consult the current pricing/access reference for tier limits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/abtdomain/skills/domain)
- [DomainKits MCP](https://domainkits.com/mcp)
- [DomainKits Pricing](https://domainkits.com/pricing)
- [DomainKits Skills](https://github.com/ABTdomain/domainkits-skills)
- [DomainKits MCP GitHub](https://github.com/ABTdomain/domainkits-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include domain availability, DNS, WHOIS/RDAP, pricing, trend, monitoring, usage, and account-bound tool results returned by DomainKits MCP.]

## Skill Version(s):

3.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
