## Description:

Runs scripts/cos_ops.py against one environment-configured Tencent COS bucket when the user explicitly requests the skill or names that bucket and object key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[onesoloapp](https://clawhub.ai/user/onesoloapp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list, upload, download, and delete single objects in the Tencent COS bucket configured by environment variables, while keeping operations bounded to approved bucket, prefix, and confirmation flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change cloud storage by uploading, overwriting, downloading, listing, or deleting objects in the configured Tencent COS bucket.

Mitigation: Use COS credentials scoped to the intended bucket and prefix, set COS_ALLOWED_PREFIX and COS_LOCAL_ROOT when possible, and review delete or overwrite requests before approving them.

Risk: Accidental object deletion or replacement can occur if a key or local path is wrong.

Mitigation: Confirm the bucket, object key, and local path before mutating operations; deletion requires --confirm to exactly match the object key, and replacements require --overwrite.

## Reference(s):

- [Tencent COS API reference](references/cos_api.md)
- [ClawHub skill page](https://clawhub.ai/onesoloapp/skills/tencent-cos-ops)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute bounded Tencent COS upload, download, list, and single-object delete commands when the user explicitly approves mutating actions.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
