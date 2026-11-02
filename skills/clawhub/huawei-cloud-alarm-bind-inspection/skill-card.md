## Description:

Inspects Huawei Cloud CES and AOM alarm binding coverage against metric and event baselines and generates instance-level reports and remediation suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud developers and operations engineers use this skill to compare configured CES and AOM alarms with account resource baselines, assess binding coverage, and review generated remediation suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials and generated reports may expose account or resource information.

Mitigation: Use a dedicated read-only cloud identity and keep credentials and reports private.

Risk: The SDK and CLI could target different cloud accounts, making audit results misleading.

Mitigation: Confirm both tools use the intended same account before running the inspection.

Risk: Unverified CLI downloads or optional uninstall steps could compromise the environment or remove stored profiles.

Mitigation: Verify CLI downloads before execution and back up ~/.hcloud before using optional uninstall instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-alarm-bind-inspection)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/wtsnew-hcli/index.html)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Guidance]

**Output Format:** [Instance-level Excel reports and an HTML report with alarm-binding findings and remediation suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cover CES and AOM metric and event baselines.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
