## Description:

Checks Redis cluster nodes-*.conf metadata files for seven integrity issue categories that can cause instance startup failures, connection anomalies, and fault alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect Huawei Cloud MRS Redis cluster metadata files, diagnose startup or connection anomalies, and produce check results with repair guidance when issues are found.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest production repair commands that stop Redis services or move, copy, edit, and remove Redis metadata files.

Mitigation: Treat such commands as operator guidance requiring independent validation, current backups, and explicit approval before execution.

Risk: The security summary classifies the release as suspicious because static analysis guidance is paired with potentially mutating repair steps.

Mitigation: Use the diagnostic report for review first, and separate analysis from any production change process.

## Reference(s):

- [IAM Policies - MRS Redis Meta Check](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown report with check results and optional repair guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local Redis metadata analysis from user-provided nodes-*.conf content; repair commands should be reviewed before use.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
