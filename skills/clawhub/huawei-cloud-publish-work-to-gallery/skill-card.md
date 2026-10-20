## Description:

Helps users prepare and publish a project to the Huawei Cloud University Operations Platform gallery or an activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project owners use this skill to prepare a project submission, select an eligible activity, and publish their work to the Huawei Cloud gallery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publishing workflow accesses local project files and uploads screenshots and other project artifacts.

Mitigation: Review the selected project and generated artifacts before approving publication.

Risk: Huawei AK/SK and temporary STS credentials are used during publication.

Mitigation: Use minimum necessary permissions, keep credentials local, and delete temporary STS files after use.

Risk: GitCode authentication may persist credentials on the machine.

Mitigation: Review the OAuth authorization step and avoid running it on shared machines.

Risk: Environment setup may install external tools through downloaded scripts.

Mitigation: Verify installer sources manually rather than running unreviewed download-and-execute commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-publish-work-to-gallery)
- [Gallery API specification](references/api-spec.md)
- [Work preparation](references/work-preparation.md)
- [IAM permission requirements](references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown publishing result and gallery URL; PNG cover and ZIP work details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the published work URL and reward status when available.]

## Skill Version(s):

1.0.2 (source: ClawHub server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
