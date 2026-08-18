## Description:

Read-only diagnostics for Alibaba Cloud CDN refresh and preload issues, verifying task records and edge cache status and producing an evidence-based diagnosis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate Alibaba Cloud CDN refresh or preload operations that appear ineffective, failed, or stale. It helps confirm task records, cache status, origin behavior, and recommended corrective actions without submitting refresh or preload jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically enumerate CDN task records across all domains visible to the current aliyun CLI credentials when input is incomplete.

Mitigation: Install only where those credentials are permitted to read CDN refresh and preload task history, prefer explicit URL or domain inputs, and avoid no-parameter mode in shared or highly privileged accounts.

Risk: Diagnostic output may include task URLs, AccountId, Arn, and probe output that expose sensitive operational details.

Mitigation: Treat generated reports and probe output as sensitive operational data and share them only with authorized recipients.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cdn-refresh-preload)
- [CDN Cache Rules Reference](references/cache-rules.md)
- [Cross-Skill Diagnostic Linkage](references/diagnosis-tree.md)
- [Probe Result Routing and Text Diagnosis Reference](references/probe-result-routing.md)
- [RAM Policies Required](references/ram-policies.md)
- [Diagnostic Report Template](references/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown diagnostic report with inline shell commands and optional JSON script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Declares any auto-filled UID, domain, URL, or role name in the final report.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
