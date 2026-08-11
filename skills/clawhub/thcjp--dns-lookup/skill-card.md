## Description:

使用 bind-utils 的 dig 命令将主机名解析为 IP 地址，支持中文交互，用于域名排查和自动化工作流集成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations engineers, and automation users use this skill to run DNS lookups with dig, resolve hostnames to IP addresses, and troubleshoot DNS records, trace paths, TTLs, timeouts, and connectivity issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and command execution capabilities beyond a narrow DNS lookup helper.

Mitigation: Restrict use to explicit DNS lookup and troubleshooting tasks, and review shell commands before execution.

Risk: The artifact includes unrelated API, file-processing, and marketing-workflow guidance that can broaden the expected behavior.

Mitigation: Treat non-DNS behavior as out of scope unless the user gives direct confirmation for a specific file, API, marketing, or unrelated shell task.

Risk: Generic API_KEY setup guidance may encourage unnecessary credential configuration for DNS lookup use cases.

Mitigation: Do not configure a generic API_KEY for this skill unless a reviewed workflow explicitly requires it, and prefer least-privilege credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dns-lookup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown or JSON-like text with DNS lookup results, dig command guidance, and troubleshooting notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DNS records, IP addresses, TTLs, trace details, timeout settings, error summaries, and next-step guidance.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
