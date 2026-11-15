## Description:

Submits sandbox or ECS deployment links to Huawei Cloud's open capability challenge through its production API and guides users through optional gallery publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to submit a sandbox site or ECS public URL for the Huawei Cloud open capability challenge. It validates the relevant link details, reports submission status, and explains optional follow-up steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The submission workflow includes unrelated CLI installation or updates, persistent changes, unpinned downloads, and script behavior that security scanners could not fully inspect.

Mitigation: Avoid installation until the unrelated CLI and gallery installer have been removed or independently reviewed and pinned, and the submission script has been fully assessed. If proceeding, consider the user's permissions, cloud credentials, terminal logs, and possible external reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-activity-submit)
- [Huawei Cloud activity submission API](https://open-dataset.huaweicloud.com/api/v1/hdopenservice/agent)
- [Optional gallery publishing skill source](https://gitcode.com/Lingxi-HandsOn/gallery.git)
- [CLI installation guide](artifact/references/cli-installation-guide.md)
- [Credential and IAM guidance](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Shell commands]

**Output Format:** [HTTPS JSON requests with text status and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits one challenge milestone per invocation and reports the expected points subject to the service's actual award.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
