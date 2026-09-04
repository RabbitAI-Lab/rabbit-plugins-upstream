## Description:

查询华为云CDM（Cloud Data Migration）资源详情，包括集群列表、集群详情、任务列表和任务执行历史

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to query Huawei Cloud CDM clusters, job lists, job details, and execution history during routine inspection, troubleshooting, or automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Huawei Cloud AK/SK environment variables to query CDM metadata.

Mitigation: Use least-privilege read-only credentials and install the skill only when the agent should access Huawei Cloud CDM metadata.

Risk: The artifact references supporting scripts and documentation that are not present in the inspected package.

Mitigation: Confirm required setup files and runtime dependencies before relying on the skill in an operational workflow.

## Reference(s):

- [Huawei Cloud CDM API Reference](https://support.huaweicloud.com/api-cdm/index.html)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub Skill Page](https://clawhub.ai/yangaiwu/skills/test-field-files)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides read-only Huawei Cloud CDM queries using user-provided project, region, cluster, and job identifiers.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
