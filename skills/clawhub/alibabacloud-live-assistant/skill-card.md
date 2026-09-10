## Description:

Read-only diagnostics for Alibaba Cloud Live covering stream quality checks, CDN edge-node probing, local recording or snapshots, traffic-theft analysis, and signed push/pull test URL generation without changing Live configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and support engineers use this skill to diagnose Alibaba Cloud Live streaming issues, inspect CDN node behavior, investigate suspected traffic theft, generate signed test URLs, and capture local stream evidence. It is intended for user-provided streams or domains and provides evidence-based findings and manual remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports under-disclosed external lookups and network-probing behavior.

Mitigation: Review before installing in sensitive environments, avoid --verbose unless disclosure of node IPs to ipinfo.io is acceptable, and run probes only against explicitly authorized user-provided targets.

Risk: Origin tracing can infer and probe targets beyond the originally supplied playback endpoint.

Mitigation: Use --trace-origin only when the inferred target is explicitly authorized, and prefer the documented confirmation flow before any diagnosis.

Risk: Generated signed push/pull URLs and downloaded access logs can expose sensitive stream or traffic information.

Mitigation: Treat signed URLs and logs as sensitive, use bounded trusted log windows, and avoid sharing raw secrets or downloaded logs outside authorized channels.

Risk: Alibaba Cloud API access may exceed the minimum needed if broad RAM policies are used.

Mitigation: Use the least-privilege RAM actions documented in the artifact and avoid wildcard or write permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-live-assistant)
- [RAM Policies (Read-Only)](references/ram-policies.md)
- [Security Hardening Guide](references/security-hardening-guide.md)
- [Stream Quality Troubleshooting Guide](references/stream-quality-troubleshooting.md)
- [Alibaba Cloud Live Security Overview](https://help.aliyun.com/zh/live/user-guide/security-overview/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown summaries with inline shell commands, JSON diagnostic output, generated signed URLs, and optional local media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud operations are read-only; recording and snapshot workflows may write media files to a user-specified local path.]

## Skill Version(s):

0.0.1 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
