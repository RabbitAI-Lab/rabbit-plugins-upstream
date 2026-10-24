## Description:

Inspects Huawei Cloud tenant risks across Optimization Advisor, Config, and SecMaster and produces consolidated inspection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and security engineers use this skill to collect tenant risk and compliance findings from Huawei Cloud Optimization Advisor, Config, and SecMaster, then review consolidated HTML and Excel reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-controlled metadata in generated HTML or Excel reports may become executable content.

Mitigation: Validate or fix HTML script-data escaping and spreadsheet formula neutralization before opening or sharing reports, especially where other tenant users can create or rename resources.

Risk: Inspection access and generated reports expose sensitive tenant information.

Mitigation: Use least-privilege Huawei Cloud credentials and restrict access to generated reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-oa-risk-inspection)
- [Huawei Cloud Optimization Advisor documentation](https://support.huaweicloud.com/productdesc-oa/oa_01_0002.html)
- [Huawei Cloud Config documentation](https://support.huaweicloud.com/rms/index.html)
- [Huawei Cloud SecMaster documentation](https://support.huaweicloud.com/secmaster/index.html)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM authentication guide](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and generated HTML/XLSX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports contain tenant risk and compliance findings; handle as sensitive data.]

## Skill Version(s):

1.0.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
