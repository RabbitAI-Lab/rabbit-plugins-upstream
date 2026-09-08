## Description:

Read-only skill for querying Huawei Cloud EVS disk lists and monitoring metrics such as IOPS, throughput, and latency using Huawei Cloud KooCLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to list Huawei Cloud EVS disks and inspect read-only Cloud Eye monitoring metrics for a configured account and region. It helps agents produce KooCLI-based query commands and summarize disk inventory, IOPS, throughput, and latency details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads Huawei Cloud EVS inventory and monitoring data, which may expose account infrastructure details if broad credentials are used.

Mitigation: Configure hcloud with the documented read-only IAM permissions and avoid broad account credentials.

Risk: The artifact references wrapper scripts that were not included in the supplied artifact.

Mitigation: Review any separately supplied scripts before use and keep agent execution limited to the disclosed read-only KooCLI operations.

Risk: Credential material could be exposed if AK/SK values are hardcoded or logged.

Mitigation: Use hcloud configuration or environment-based credential loading and do not write credentials to scripts, configuration files, logs, or agent output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huawei-cloud-evs-detail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud EVS and CES query guidance; requires hcloud credentials and appropriate IAM permissions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
