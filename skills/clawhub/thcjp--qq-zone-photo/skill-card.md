## Description:

社交空间相册 helps an agent guide QR-code login, album browsing, photo upload and download, and album creation for social-space photo albums using session-cookie based automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to automate routine social-space photo album tasks such as logging in, listing albums, uploading photos, downloading photos, and creating albums.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on full-access session cookies for social-space album operations.

Mitigation: Keep cookies.json private with restrictive file permissions, avoid sharing or backing it up, and refresh or revoke the session if exposure is possible.

Risk: The skill uses non-official APIs that may change or behave unexpectedly.

Mitigation: Review the skill before installation and confirm each upload, album creation, or full-album download before allowing an agent to execute it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/qq-zone-photo)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may reference local cookie files, album IDs, photo URLs, and image paths supplied by the user.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
