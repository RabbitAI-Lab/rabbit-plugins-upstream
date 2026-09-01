## Description:

Analyze local pcap/pcapng captures to diagnose network transfer, connection, VPN/IPsec, DNS, TLS, MTU, packet-size, and session anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, network engineers, and operations teams use this skill to analyze user-provided pcap/pcapng captures and generate a structured diagnosis for slow transfers, connection failures, VPN/IPsec negotiation issues, DNS/TLS failures, MTU problems, and TCP window or retransmission anomalies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Packet captures can contain sensitive network metadata and payload fragments, and untrusted captures may not be suitable for analysis on sensitive machines.

Mitigation: Analyze only pcap files the user intentionally provides, prefer an isolated virtual environment for Scapy, and avoid running untrusted captures on sensitive hosts.

Risk: The --output option writes a Markdown report and can overwrite an existing file at the chosen path.

Mitigation: Use a fresh report filename or confirm the output path before running the analyzer.

Risk: Incomplete captures can limit or skew RTT, retransmission, and connection-state conclusions.

Mitigation: Prefer captures that include the relevant complete TCP streams, including SYN/SYN-ACK handshakes, and use --src, --dst, or --port to focus multi-session captures.

## Reference(s):

- [Analysis Rules](references/analysis-rules.md)
- [Report Structure](references/report-structure.md)
- [Limitations](references/limitations.md)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-pcap-analyzer)

## Skill Output:

**Output Type(s):** [markdown, shell commands, guidance]

**Output Format:** [Markdown diagnosis report, with shell commands used to run the local analyzer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is printed to stdout by default or written to a user-selected Markdown file with --output.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
