## Description:

Guides agents through signing and uploading local documents to an ima knowledge base via temporary COS credentials, including troubleshooting upload failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dzz-777](https://clawhub.ai/user/dzz-777)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to upload selected local documents to an ima knowledge base and troubleshoot COS signature or authorization failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading unintended or sensitive local documents to a knowledge base.

Mitigation: Review file paths, knowledge_base_id, and folder_id before uploading; only select documents appropriate for that knowledge base.

Risk: Temporary COS credentials could remain in local files after an upload.

Mitigation: Delete temporary credential files immediately after uploading.

Risk: Repeated uploads or mismatched replacement titles can create duplicate knowledge-base entries.

Mitigation: Check existing titles before retrying and match the full title exactly when replacing an entry.

## Reference(s):

- [ima homepage](https://ima.qq.com)
- [ClawHub skill release](https://clawhub.ai/dzz-777/skills/ima-mcp-cos-upload)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Python and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes upload checks and troubleshooting guidance.]

## Skill Version(s):

1.0.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
