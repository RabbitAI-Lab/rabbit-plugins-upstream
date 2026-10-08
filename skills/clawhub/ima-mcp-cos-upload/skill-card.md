## Description:

Guides agents through direct Tencent COS uploads to an ima knowledge base and troubleshooting of upload authorization errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dzz-777](https://clawhub.ai/user/dzz-777)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers uploading selected Markdown, PDF, or presentation files to personal or shared ima knowledge bases can use this skill to follow the signed COS upload workflow and diagnose 403 errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upload sends a local file to an unintended knowledge base or folder.

Mitigation: Confirm the exact file, destination knowledge base, and folder before uploading.

Risk: Temporary COS credentials or authorization headers are exposed in shared chats, logs, shell history, or leftover files.

Mitigation: Keep credentials and headers out of shared chats, logs, and shell history; delete temporary credential files after use.

Risk: Repeating an upload can create duplicate knowledge-base entries.

Mitigation: Check for an existing item before retrying and verify the resulting entry after upload.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dzz-777/skills/ima-mcp-cos-upload)
- [ima homepage](https://ima.qq.com)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Python and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upload and verification steps for user-selected files; no automatic file output.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
