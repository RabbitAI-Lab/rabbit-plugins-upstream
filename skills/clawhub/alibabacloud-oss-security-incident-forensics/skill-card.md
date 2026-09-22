## Description:

Read-only forensics for Alibaba Cloud OSS traffic abuse and security incidents, including exposure checks, real-time log analysis, root-cause routing, and containment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud support engineers, security responders, and developers use this skill to investigate OSS traffic spikes, suspected AccessKey leaks, hotlinking, and suspicious bucket activity without changing customer resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use cloud credentials to read OSS configuration metadata and OSS real-time-log request metadata, and may enumerate bucket names when no bucket is supplied.

Mitigation: Install it with short-lived, least-privilege Alibaba Cloud credentials, provide the bucket name whenever possible, and scope RAM permissions to the known bucket and log project.

Risk: Forensic conclusions may be incomplete when permissions, network access, or real-time-log availability cause a degraded report.

Mitigation: Treat degraded output as limited, review the recorded errors, and use the emitted SLS query sequence or enable real-time logs before relying on final attribution.

Risk: Containment recommendations affect live access paths if applied manually without review.

Mitigation: Review suggested ACL, Referer, Block Public Access, and AccessKey changes against legitimate consumers before applying them in Alibaba Cloud controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-oss-security-incident-forensics)
- [Traffic-Abuse Forensics Playbook](references/traffic-abuse-playbook.md)
- [Bucket Exposure-Surface Check](references/exposure-check.md)
- [Minimal Read-Only RAM Policy](references/ram-policies.md)
- [Alibaba Cloud OSS traffic fees documentation](https://help.aliyun.com/zh/oss/traffic-fees)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured status, findings, next actions, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces evidence-based forensic conclusions, degraded-status limitations, auto-filled parameter declarations, and manual containment checklists.]

## Skill Version(s):

0.0.1 (source: release evidence and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
