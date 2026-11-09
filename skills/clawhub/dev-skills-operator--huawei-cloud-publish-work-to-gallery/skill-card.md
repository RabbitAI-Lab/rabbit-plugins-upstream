## Description:

Publishes a user's project to the Huawei Cloud University Operations Platform gallery or an activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to prepare and submit a project to the Huawei Cloud University Operations Platform gallery or an activity, then receive the submission result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports credential exposure and incomplete analysis.

Mitigation: Review credential handling and requested system changes before installing or authenticating; keep credentials out of committed project files.

Risk: The workflow publishes project materials to an external gallery.

Mitigation: Review the repository, generated cover, detail archive, and selected activity before confirming publication.

Risk: The security review reports unsafe installation and publishing practices, as well as capabilities beyond the stated purpose.

Mitigation: Review installer sources and publication steps before use, and use the skill only when this specific workflow is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-publish-work-to-gallery)
- [Huawei Cloud Gallery API specification](references/api-spec.md)
- [IAM policies and temporary credentials](references/iam-policies.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [API Calls, Files, Text]

**Output Format:** [Gallery submission, PNG cover, ZIP detail archive, and text confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may require user choices and OAuth authorization; unattended environments may need manual verification.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
