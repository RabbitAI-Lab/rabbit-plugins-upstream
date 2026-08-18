## Description:

Investigate an explicitly supplied public IPv4 or IPv6 address and create an auditable multi-source ownership, routing, geolocation, proxy/VPN/Tor, abuse, fraud, hosting, reputation, and purity assessment with a portable interactive HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jianfuli](https://clawhub.ai/user/jianfuli)

### License/Terms of Use:

MIT

## Use Case:

Developers, security analysts, and operations teams use this skill to investigate a supplied public IP address, reconcile provider disagreement, and produce auditable evidence for ownership, routing, geolocation, reputation, and network-exposure decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Investigated IP addresses are sent to selected third-party intelligence providers during lookup.

Mitigation: Review the provider list before use and apply provider include or exclude options when a provider should not receive the target IP.

Risk: Existing provider API credentials in the environment may be used automatically.

Mitigation: Review the runtime environment before execution and exclude providers whose credentials or accounts should not be used.

Risk: Local JSON and HTML reports can contain detailed provider responses, especially when raw payload output is requested.

Mitigation: Avoid raw payload output unless necessary and store generated reports according to the sensitivity of the investigation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jianfuli/skills/ip-intelligence-fusion)
- [Publisher profile](https://clawhub.ai/user/jianfuli)
- [Fusion methodology](artifact/references/methodology.md)
- [Provider reference](artifact/references/providers.md)
- [Public-page collection](artifact/references/public-pages.md)
- [HTML report design](artifact/references/report-design.md)
- [Project repository link in artifact documentation](https://github.com/GetIPProxy/ip-intelligence-fusion)
- [GetIPProxy](https://getipproxy.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance]

**Output Format:** [Concise Markdown brief plus local JSON evidence and a self-contained offline HTML report; optional JSON, HTML, or Markdown output on request.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are written locally; raw upstream payloads are excluded by default and should be included only when needed.]

## Skill Version(s):

1.3.1 (source: server release evidence, README badge, and scripts/ip_intelligence.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
