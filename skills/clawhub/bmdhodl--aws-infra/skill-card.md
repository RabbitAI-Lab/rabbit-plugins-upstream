## Description: <br>
Chat-based AWS infrastructure assistance using AWS CLI and console context for querying, auditing, and monitoring AWS resources, with explicit confirmation required before write or destructive actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bmdhodl](https://clawhub.ai/user/bmdhodl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, cloud engineers, and operators use this skill to inspect AWS account state, troubleshoot resources, review security posture, check costs, and prepare safe AWS CLI actions for explicit approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect AWS resources through the user's local AWS CLI, which may expose sensitive account, resource, billing, or configuration details to the agent session. <br>
Mitigation: Use a dedicated read-only or least-privileged AWS profile, confirm the intended account and region before queries, and avoid sharing secrets or session tokens. <br>
Risk: Incorrectly approved write, delete, IAM, billing, or scaling commands could change production AWS resources. <br>
Mitigation: Review exact proposed commands before approval, prefer dry-run modes when available, and require explicit confirmation before any write or destructive action. <br>


## Reference(s): <br>
- [AWS CLI Query Patterns](references/aws-cli-queries.md) <br>
- [ClawHub AWS Infra skill page](https://clawhub.ai/bmdhodl/skills/aws-infra) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, shell commands, guidance] <br>
**Output Format:** [Markdown with inline AWS CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only AWS CLI queries are preferred; write, delete, IAM, billing, and scaling actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
