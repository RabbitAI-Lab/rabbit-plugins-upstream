## Description:

Guides an agent through visible-browser capture of segmented streaming media URLs, parallel download of video fragments, lossless MP4 merge, verification, and user-approved cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sedey999](https://clawhub.ai/user/sedey999)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to download segmented streaming videos they are authorized to save, especially videos that require visible user intervention for login, verification, viewing passwords, or quality selection. It is most mature for Youku workflows and includes guidance for capture, probing, parallel download, merge validation, and cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser sessions, passwords, cookies, and exported diagnostic files may expose sensitive account data.

Mitigation: Use a dedicated browser profile, avoid entering high-risk accounts or passwords, and delete cookies.json, dom.txt, and pwinfo.txt after use.

Risk: The skill can collect protected media URLs and download restricted streaming content.

Mitigation: Use it only for content the user is authorized to save, and review the applicable copyright and platform terms before running downloads.

Risk: Intermediate video fragments may remain on disk and contain recoverable media content.

Mitigation: Keep fragments until the merged file is validated, then run the cleanup workflow after explicit user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sedey999/skills/video-downloader-by-browser)
- [Youku reference notes](references/youku.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and local file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser logs, captured media URL metadata, downloaded fragments, merged MP4 files, verification reports, and cleanup commands.]

## Skill Version(s):

1.1.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
