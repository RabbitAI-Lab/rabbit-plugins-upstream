## Description:

域名DNS helps agents manage domain and DNS operations across Cloudflare, DNSimple, and Namecheap, including DNS lookups, zone onboarding, record changes, and bulk import or export workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation teams use this skill to plan and perform DNS/domain administration tasks, inspect records and TTLs, and prepare operational logs or configuration guidance. It is intended for workflows that can safely use cloud/DNS credentials and agent file, command, and network access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file, command, network, and cloud-credential access for DNS/domain automation.

Mitigation: Install only when that access is intended, use least-privilege DNS/cloud credentials, and review the agent's plan before allowing operations.

Risk: DNS record changes, domain registration, imports, exports, monitoring, and deployment actions can alter production infrastructure or incur costs.

Mitigation: Require explicit confirmation for each state-changing action and verify target domains, zones, records, providers, and billing impact before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/domain-dns-ops)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON-style responses with operational guidance and command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose DNS/domain state changes that require explicit user review and confirmation before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
