## Description:

Live-Debug runtime diagnostics: dynamic logging, method snapshots, dynamic metrics, dynamic spans, and JVM inspection for Alibaba Cloud CMS ServiceTask workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to create, inspect, delete, and query Alibaba Cloud Live-Debug ServiceTask diagnostics for Java and Python services. It helps operators add dynamic logs, snapshots, metrics, spans, and JVM inspection commands while checking required Alibaba Cloud CLI, CMS, SLS, and RAM prerequisites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add diagnostic probes to running Alibaba Cloud services and collect broad runtime data.

Mitigation: Install it only for authorized operators, confirm exact service and instance IDs before creating probes, and avoid wildcard production targets unless explicitly approved.

Risk: Live-Debug captures can expose sensitive request, authentication, payment, or user data.

Mitigation: Keep TTL and capture counts low, avoid sensitive fields in probe expressions and templates, query only the required SLS logs, and remove probes promptly after diagnosis.

Risk: The artifact includes commands that delete ServiceTask probes or tasks.

Mitigation: Use the documented two-phase delete flow: present exact targets and impact first, then execute only after explicit user approval.

## Reference(s):

- [Live-Debug Module](references/live-debug.md)
- [RAM Policy Reference](references/ram-policies.md)
- [Alibaba Cloud CLI Documentation](https://help.aliyun.com/document_detail/121541.html)
- [Alibaba Cloud CLI Install Guide](https://help.aliyun.com/zh/cli/install-cli)
- [Alibaba Cloud CLI Update Guide](https://help.aliyun.com/zh/cli/update-cli)
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-livedebug)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON task configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Alibaba Cloud CLI commands, RAM policy snippets, probe/task JSON, and SLS query guidance.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
