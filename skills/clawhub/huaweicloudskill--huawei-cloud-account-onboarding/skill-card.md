## Description:

Guides Huawei Cloud customers through read-only real-name authentication status checks and user-requested face-verification QR code retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud customers and support agents use this skill to check real-name verification status and, when requested, obtain a QR code for the customer to complete face verification on their own device.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account access keys and QR-code URLs can expose sensitive authentication information.

Mitigation: Use the narrowest available BSS read-only credentials, keep access keys out of permanent shell files, and treat QR-code URLs as sensitive.

Risk: The optional KooCLI installation step runs a downloaded installer.

Mitigation: Review the optional installer before running it; the skill's authentication checks use the Python SDK.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-account-onboarding)
- [Huawei Cloud real-name authentication status API](https://support.huaweicloud.com/api-oce/mac_00006.html)
- [Huawei Cloud real-name authentication QR code API](https://support.huaweicloud.com/api-oce/mac_00005.html)
- [IAM policies](references/iam-policies.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and status or QR-code URL results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [QR-code URLs are single-use and expire after 10 minutes; the customer completes verification on their own device.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
