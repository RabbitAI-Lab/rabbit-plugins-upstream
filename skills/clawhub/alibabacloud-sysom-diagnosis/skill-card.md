## Description:

Use when troubleshooting Linux server performance or stability issues across CPU saturation, high load, scheduling delay, memory pressure, OOM events, high RSS, cache or shared-memory growth, Java heap issues, disk IO latency, packet loss, network jitter, or an unstable server; it performs diagnosis and surfaces recommendations without applying fixes automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose Alibaba Cloud Linux or ECS performance and stability issues across memory, IO, load/CPU, network, and Java runtime domains. The skill guides SysOM CLI collection, interprets Agent-facing envelopes, and returns evidence-based operational recommendations without executing repairs automatically.

### Deployment Geography for Use:

China Mainland and China (Hong Kong)

## Known Risks and Mitigations:

Risk: The skill may install and run the sysom-osops CLI with sudo and use remote SysOM diagnostic access.

Mitigation: Install only for Alibaba Cloud Linux/ECS diagnosis, review the installer source and environment fit, and keep remediation actions separate from diagnosis unless explicitly requested.

Risk: Remote diagnosis requires Alibaba Cloud credentials or an ECS RAM Role.

Mitigation: Configure credentials outside the chat and use the least-privilege RAM actions documented for SysOM access.

Risk: Java profiling and collection follow-ups can run for several minutes and may add sampling or agent overhead to the target process.

Mitigation: Explain duration and expected impact, obtain user confirmation before long-running profiling, run the requested command once, and avoid duplicate collection after client timeouts.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/sdk-team/skills/alibabacloud-sysom-diagnosis)
- [SysOM diagnosis workflow](artifact/SKILL.md)
- [Supported environments](artifact/references/supported-environments.md)
- [RAM policies](artifact/references/ram-policies.md)
- [Deep actions reference](artifact/references/deep-actions.md)
- [Report interpretation](artifact/references/report-interpretation.md)
- [Java diagnosis reference](artifact/references/java/README.md)
- [Java memory diagnosis guide](artifact/references/java/memory/memory-guide.md)
- [Java profiling playbook](artifact/references/java/memory/profiling-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnostic responses with command progress, evidence summaries, and recommended next actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not apply fixes automatically; remote diagnosis requires sysom-osops, Alibaba Cloud credentials, Cloud Assistant on the target ECS instance, and supported regions.]

## Skill Version(s):

0.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
