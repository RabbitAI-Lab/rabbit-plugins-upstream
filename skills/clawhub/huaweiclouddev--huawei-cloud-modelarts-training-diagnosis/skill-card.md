## Description:

Diagnoses failed, timed-out, abnormal, or stuck Huawei Cloud ModelArts training jobs by collecting hcloud CLI job details, events, stages, and logs and returning root-cause conclusions, fix suggestions, and confidence levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML engineers use this skill to diagnose Huawei Cloud ModelArts training jobs that failed, timed out, became abnormal, or appear stuck. It helps collect read-only job evidence through hcloud CLI and produce actionable remediation guidance with confidence levels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use cloud credentials to discover ModelArts job metadata and diagnostic logs, including broad account scans.

Mitigation: Use a least-privilege or test Huawei Cloud profile and provide an exact job ID, region, and time window unless broad scanning is intentional.

Risk: Diagnostic logs and hcloud outputs may contain sensitive details such as raw logs, OBS log URLs, credentials, tokens, or infrastructure identifiers.

Mitigation: Redact sensitive fields and share only the minimum error lines or summarized findings needed for diagnosis.

Risk: The artifact includes shell guidance for installing and uninstalling hcloud CLI components.

Mitigation: Inspect installer sources before execution, avoid non-interactive installation unless the source is trusted, and back up hcloud configuration before cleanup commands.

## Reference(s):

- [API Catalog](references/api-catalog.md)
- [Diagnosis Flow](references/diagnosis-flow.md)
- [Command Templates](references/hcloud-command-templates.md)
- [Confidence Rules](references/confidence-rules.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud CLI Documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnosis report with tables, fix steps, and inline hcloud CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include confidence levels and should avoid exposing full logs or credentials.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
