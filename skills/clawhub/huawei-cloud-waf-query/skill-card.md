## Description:

Query Huawei Cloud WAF (Web Application Firewall) attack events, access/protection logs, attack statistics, threat overview and top attack source IPs for daily security inspection and incident troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, developers, and cloud engineers use this skill to inspect Huawei Cloud WAF events, logs, statistics, threat summaries, and top attack source IPs during daily review and incident troubleshooting. The skill helps an agent prepare read-only Huawei Cloud KooCLI commands and summarize returned WAF JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries WAF logs and event details that may contain sensitive IP addresses, domains, and security-event data.

Mitigation: Use the skill only in environments where the agent is authorized to view WAF data, and avoid exposing returned logs beyond the operational need.

Risk: Huawei Cloud credentials with broad privileges could allow more access than the read-only workflow requires.

Mitigation: Use a least-privilege WAF read-only IAM policy and avoid administrator credentials for agent execution.

Risk: Installing or updating KooCLI from a remote installer can introduce supply-chain risk.

Mitigation: Verify the CLI installer and prefer trusted package-manager or documented installation paths before running setup commands.

## Reference(s):

- [Huawei Cloud WAF Query on ClawHub](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-waf-query)
- [Publisher profile](https://clawhub.ai/user/erickeyhu-hug)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Related commands](references/related-commands.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown, text]

**Output Format:** [Markdown guidance with inline shell commands and expected JSON response shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud WAF query assistance; commands require KooCLI authentication, region, project ID, and time-window parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
