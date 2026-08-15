## Description:

Guides agents to use the installed shodan-skill CLI for documented Shodan REST, Streaming, Trends, and Exploits operations including host intelligence, search, DNS, scans, alerts, notifiers, datasets, organizations, credit checks, and real-time feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuweitao](https://clawhub.ai/user/liuweitao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and analysts use this skill to translate Shodan investigation, monitoring, scanning, and account-management requests into CLI workflows grounded in documented Shodan APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Shodan credits or change and delete Shodan account resources after a broadly matched request.

Mitigation: Review before installing when the Shodan key has paid credits, scan privileges, Enterprise access, or organization-admin rights; prefer strict safety mode or dry-run for scans, alerts, notifiers, dataset downloads, and organization changes.

Risk: A broadly privileged Shodan key increases the impact of accidental scans, monitoring changes, Enterprise downloads, or organization updates.

Mitigation: Use a least-privileged Shodan key where possible and verify account entitlements before Enterprise or mutating workflows.

Risk: Shodan API keys, authorization headers, notifier arguments, webhook URLs, and signed dataset URLs may be sensitive.

Mitigation: Keep credentials out of prompts, commands, source files, and logs, and preserve the skill's redaction behavior for credential-like values and signed URLs.

## Reference(s):

- [Skill page](https://clawhub.ai/liuweitao/skills/shodan-skill)
- [Publisher profile](https://clawhub.ai/user/liuweitao)
- [API coverage](references/api-coverage.yaml)
- [Safety and live operations](references/safety.md)
- [Search, hosts, and saved queries](references/search-and-host.md)
- [Scans, alerts, and notifiers](references/scan-and-alerts.md)
- [Enterprise operations](references/enterprise.md)
- [Streaming API](references/streaming.md)
- [Shodan REST API](https://developer.shodan.io/api)
- [Shodan Streaming API](https://developer.shodan.io/api/stream)
- [Shodan Trends API](https://developer.shodan.io/api/trends)
- [Shodan Exploits API](https://developer.shodan.io/api/exploits/rest)
- [Shodan Datapedia](https://datapedia.shodan.io/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and JSON output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SHODAN_API_KEY or official Shodan CLI configuration; CLI responses are described as stable JSON envelopes, JSON Lines streams, or SSE data events.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
