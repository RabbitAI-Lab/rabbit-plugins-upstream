## Description:

Live-Debug runtime diagnostics for Alibaba Cloud CMS ServiceTask, including dynamic logging, method snapshots, dynamic metrics, dynamic spans, JVM inspection, probe cleanup, and SLS result queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and site reliability engineers use this skill to diagnose live Alibaba Cloud services by creating, listing, querying, and deleting Live-Debug ServiceTask probes and Java JVM inspection commands. It also guides least-privilege RAM setup, CLI prerequisites, workspace and service resolution, and recovery from common service errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can instrument live services and capture sensitive runtime data.

Mitigation: Use a dedicated least-privilege RAM identity scoped to the intended workspace, service, SLS project, and logstore; avoid wildcard targets in production unless explicitly approved.

Risk: Task configurations for logs, snapshots, metrics, and spans may capture sensitive application data.

Mitigation: Review taskConfig expressions before execution, set short ttl and captureCount values, and prefer narrow target instances.

Risk: Bulk deletion can remove active probes from a service.

Mitigation: Use the documented two-phase delete flow and dry-run behavior before deleting probes.

Risk: Workflow User-Agent session identifiers are sent to Alibaba Cloud services.

Mitigation: Treat session ids as operational traceability metadata and avoid embedding secrets or user-sensitive data in them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-livedebug)
- [Live-Debug Module](references/live-debug.md)
- [RAM Policy Reference](references/ram-policies.md)
- [Alibaba Cloud CLI documentation](https://help.aliyun.com/document_detail/121541.html)
- [Alibaba Cloud CLI install guide](https://help.aliyun.com/zh/cli/install-cli)
- [Alibaba Cloud CLI update guide](https://help.aliyun.com/zh/cli/update-cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash commands and JSON task configurations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Aliyun CLI workflows and companion shell script usage for CMS ServiceTask and SLS operations.]

## Skill Version(s):

0.0.1-beta.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
