## Description:

Multi-region website availability probing and nationwide multi-ISP network testing over a public probing platform for HTTP, Ping, DNS, MTR, and traceroute diagnostics, with optional mobile 4G/5G perspective.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and network operators use this skill to check whether a website, API, domain, or IP has regional, carrier-specific, DNS, latency, packet-loss, HTTP status, or mobile access problems. The agent submits bounded public probes, saves results to JSON, and reports a concise diagnosis from the returned node data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Probe targets are sent to the public third-party probing service boce.aliyun.com.

Mitigation: Use only with targets that can be shared with that service; avoid private hosts, confidential pre-production endpoints, signed URLs, credentials, and sensitive query strings.

Risk: The skill caches anonymous boce session state under ~/.qoderwork/cache/boce_session.json.

Mitigation: Clear that cache file when removing local session state is required.

Risk: Dependency resolution may change the installed requests or urllib3 versions within the declared ranges.

Mitigation: Install in an isolated environment and use current dependency resolution or pinned lockfiles appropriate for the deployment.

## Reference(s):

- [Deep Diagnosis Rules](references/diagnostic-rules.md)
- [RAM Policies and Cloud Authorization](references/ram-policies.md)
- [Network Probe Skill - Getting Started](references/user-guide.md)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-website-probe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown diagnosis with inline shell commands and JSON result files saved to disk]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [HTTP and DNS results are interpreted through dedicated analyzer scripts; Ping, MTR, and traceroute results are summarized from the wrapper's per-node tables.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
