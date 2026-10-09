## Description:

Helps agents create, inspect, price, and manage supported Alibaba Cloud DTS database synchronization jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Database administrators and engineers use this skill to plan and manage same-account, one-way Alibaba Cloud DTS synchronization between supported cloud databases, monitor jobs, and check instance pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating synchronization jobs can provision billable DTS resources.

Mitigation: Review the plan, class, current quotation and billing impact; require explicit approval before creating or changing jobs.

Risk: The workflow can install or update local Alibaba Cloud tooling and update the skill automatically.

Mitigation: Review installation and update behavior before use; set DTS_SKILLS_AUTO_UPDATE=0 when automatic skill updates are not acceptable.

Risk: Database credentials may be stored locally as reversible Base64.

Mitigation: Protect local credential storage and use least-privilege Alibaba Cloud permissions.

Risk: PostgreSQL and MongoDB links may require non-encrypted connections.

Mitigation: Use these links only when the documented connection requirement is acceptable within the network environment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-dts-job-manager)
- [Supported synchronization links](artifact/references/supported-links.md)
- [Database credentials and connection tests](artifact/references/credentials-and-security.md)
- [DTS synchronization channel specifications](https://help.aliyun.com/en/dts/product-overview/specifications-of-data-synchronization-channels)
- [DTS billable items](https://help.aliyun.com/en/dts/product-overview/billable-items)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Job details, progress and price quotations depend on live Alibaba Cloud responses.]

## Skill Version(s):

0.0.1-beta.1 (source: ClawHub release metadata and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
