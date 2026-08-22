## Description:

Auditable, local-first intelligence for a single authorized public IPv4 or IPv6 address, producing ownership, routing, geolocation, reputation, proxy, VPN, Tor, hosting, and fraud-risk evidence for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jianfuli](https://clawhub.ai/user/jianfuli)

### License/Terms of Use:

MIT

## Use Case:

Developers, security operators, ecommerce and operations teams use this skill to check one owned, public, or otherwise authorized public IP and generate a timestamped JSON, Markdown, or offline HTML evidence report. The report supports authorized infrastructure review, public-information verification, abnormal-request triage, and network-provider delivery acceptance testing, not identity lookup or automatic allow/deny decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An IP address can become personal information when associated with a person, account, customer, employee, or login record.

Mitigation: Use the skill only for a single owned, public, or explicitly authorized public IP, and do not provide customer logs, account logs, cookies, device identifiers, fingerprints, or batch IP datasets.

Risk: External provider lookups may transmit the target IP to third-party services and may involve cross-border transfer.

Mitigation: Keep the default local-only mode unless external lookup is necessary; before using external mode, review the target IP, providers, domains, transmitted fields, and obtain explicit confirmation.

Risk: Generated reports can contain complete IP addresses, geographic regions, organization or ISP names, route prefixes, and network-risk labels.

Mitigation: Store generated reports in controlled locations with restrictive permissions, avoid public issues, demo sites, and public logs, and delete reports according to the operator's retention schedule.

Risk: Numeric or boolean reputation signals can be misread as proof of abuse or as a safe/unsafe decision.

Mitigation: Treat the output as an aid for authorized human review, preserve conflicts and source states, and do not use a report as a legal conclusion or automatic platform decision.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jianfuli/skills/ip-address-reputation-risk)
- [README](README.md)
- [Fusion methodology](references/methodology.md)
- [Provider reference](references/providers.md)
- [Public-page evidence](references/public-pages.md)
- [HTML report design](references/report-design.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated JSON, Markdown, or offline HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include policy metadata, source-state counts, timestamps, consensus facts, conflicts, contextual network-risk signals, and generated file paths; upstream raw payloads, contact details, and API keys are excluded.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
