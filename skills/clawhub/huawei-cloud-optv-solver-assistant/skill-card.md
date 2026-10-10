## Description:

Guides an agent through OptVerse mathematical optimization workflows, from requirements and data validation to solving and publishing results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations-research practitioners use this skill to model and solve optimization problems with Huawei Cloud OptVerse, review intermediate artifacts, and publish the resulting asset. Optional steps deploy and test the published service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud credentials and cached tokens can expose account access.

Mitigation: Use a minimally scoped IAM user; never display the credentials file, and clear cached token files after use.

Risk: Uploads, asset publication, and optional service deployment can affect cloud resources and expose sensitive data.

Mitigation: Review inputs and generated artifacts before publishing; avoid sensitive datasets until TLS verification and path confinement are fixed.

Risk: Unattended approval can advance workflow stages without user review.

Mitigation: Run interactively and confirm each stage unless unattended approval is intentional.

## Reference(s):

- [API Reference](references/api-reference.md)
- [Workflow Design](references/workflow-design.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files, JSON]

**Output Format:** [Conversational guidance and commands, with downloadable optimization artifacts and a published asset ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intermediate artifacts require review; deployment and service testing are optional.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
