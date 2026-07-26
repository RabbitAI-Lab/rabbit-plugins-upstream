## Description: <br>
Manage files across cloud providers with authentication, cost awareness, and multi-provider operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to upload, list, download, cost-review, and migrate cloud-storage objects across providers such as AWS, Azure, GCP, and Aliyun. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-storage operations can affect remote accounts, buckets, objects, permissions, and billable resources. <br>
Mitigation: Use only for explicit user-directed cloud-storage tasks, and verify the provider, account, bucket, region, permissions, and expected cost before execution. <br>
Risk: The documentation mixes cloud-storage behavior with SQL and database task language. <br>
Mitigation: Do not use the skill for SQL or database requests until the documentation is corrected; limit use to cloud-storage operations. <br>
Risk: Mutating actions such as upload, migration, or permission changes may have persistent effects. <br>
Mitigation: Require user confirmation before mutating operations and review the configured cloud credentials and CLI context first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/cloud-storage) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON result examples and shell-command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce cloud resource URLs, storage metadata, migration status, integrity checks, and cost reports.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; skill frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
