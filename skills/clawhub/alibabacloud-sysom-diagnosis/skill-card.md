## Description:

Troubleshoots Linux server performance and stability issues across CPU, load, memory, Java, disk IO, and network symptoms using SysOM diagnosis output, then surfaces recommendations without applying fixes automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations engineers use this skill to diagnose Linux ECS performance and stability incidents, interpret SysOM envelopes, and choose focused follow-up actions across memory, IO, load/CPU, network, and Java domains.

### Deployment Geography for Use:

China Mainland and China (Hong Kong)

## Known Risks and Mitigations:

Risk: The skill can direct installation of a missing SysOM CLI through a remote script executed with elevated privileges.

Mitigation: Confirm trust in the SysOM installer source before installation and use a manually reviewed, pinned, or signed installation path; do not let the agent run the sudo installer automatically.

Risk: Remote diagnosis requires Alibaba Cloud credentials or an ECS RAM Role.

Mitigation: Use the narrowest RAM role or policy available and configure credentials outside the agent conversation.

Risk: Long-running Java profiling may affect production workloads or take several minutes to complete.

Mitigation: Confirm profiling with the user before it runs and explain expected duration and target-process impact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-sysom-diagnosis)
- [Supported Environments](references/supported-environments.md)
- [Deep Actions Reference](references/deep-actions.md)
- [RAM Policies](references/ram-policies.md)
- [Report Interpretation](references/report-interpretation.md)
- [Java Application Diagnosis Reference](references/java/README.md)
- [Java Profiling Playbook](references/java/memory/profiling-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown diagnostic summaries with SysOM command guidance and operational recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not apply fixes automatically; long-running Java profiling requires user confirmation before execution.]

## Skill Version(s):

0.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
