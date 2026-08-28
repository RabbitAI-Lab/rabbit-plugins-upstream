## Description:

Investigate an Alibaba Cloud AccessKey leakage incident and produce a read-only investigation report with risk assessment and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, cloud engineers, and incident responders use this skill to investigate a reported Alibaba Cloud AccessKey leak, correlate account audit evidence, and produce a read-only incident report with manual remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can query broader account audit and identity data than a narrow leaked-key check suggests.

Mitigation: Run it only with a least-privilege read-only Alibaba Cloud policy and confirm the target account, region, leaked AccessKey, and lookback window before execution.

Risk: The generated report, stderr logs, and audit correlation session ID can contain sensitive incident context.

Mitigation: Store and share generated investigation artifacts as sensitive security records, and mask credentials or tokens in any downstream handling.

Risk: Runtime dependency installation can change the execution environment if AK_LEAK_AUTO_INSTALL is enabled.

Mitigation: Keep AK_LEAK_AUTO_INSTALL unset unless runtime package installation has been explicitly approved for the environment.

Risk: Empty results may reflect account-scope mismatch rather than proof that a leaked AccessKey is safe.

Mitigation: Authenticate with the account that owns the AccessKey and surface any account mismatch warning in the final investigation summary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-ak-leak-incident-response)
- [Investigation flow](references/investigation_flow.md)
- [ActionTrail audit module](references/module3_actiontrail_audit.md)
- [Timeline report module](references/module4_timeline_report.md)
- [Remediation best practices](references/module5_remediation_best_practices.md)
- [Read-only RAM policies](references/ram-policies.md)
- [Alibaba Cloud AccessKey restrictive protection description](https://www.alibabacloud.com/help/en/ram/user-guide/accesskey-restrictive-protection-description)
- [Alibaba Cloud solution to AccessKey leakage](https://www.alibabacloud.com/help/en/ram/user-guide/solution-to-accesskey-leakage)
- [Alibaba Cloud AccessKey leak detection](https://www.alibabacloud.com/help/en/security-center/user-guide/detection-of-accesskey-pair-leaks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown incident report with a fixed six-section structure and manual remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is generated from read-only Alibaba Cloud audit queries and should be treated as a sensitive investigation artifact.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
