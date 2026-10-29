## Description:

Submits sandbox and ECS work links to the Huawei Cloud open-capability challenge and reports the submission status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to submit sandbox deployment links and ECS public URLs for the Huawei Cloud open-capability challenge. It reports the result and leaves optional gallery publication and cloud-resource cleanup under the user's control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud-resource cleanup could delete resources beyond the intended challenge deployment.

Mitigation: Skip cleanup unless the user confirms the exact resources, account, and region to delete; remove only the confirmed resources.

Risk: The submission uses secret-key credentials, and printing a credential during verification could expose it.

Mitigation: Use short-lived, minimally privileged credentials over HTTPS, keep secrets out of repositories and logs, and check credential presence without printing values.

Risk: The optional gallery flow installs an external skill and may publish project code.

Mitigation: Ask for the user's consent, review and pin the installer and skill, keep cloud credentials out of the installation environment, and confirm what code will be published.

## Reference(s):

- [Huawei Cloud activity submission API](https://open-dataset.huaweicloud.com/api/v1/hdopenservice/agent)
- [Gallery publishing skill repository](https://gitcode.com/Lingxi-HandsOn/gallery.git)
- [IAM policies and credentials](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [API calls, Text, Guidance]

**Output Format:** [JSON API submissions and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits one selected challenge milestone and reports its status; does not produce a standalone file.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
