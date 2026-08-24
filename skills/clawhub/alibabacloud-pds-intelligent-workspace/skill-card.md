## Description:

Guides agents through Alibaba Cloud PDS cloud-drive operations, including file search, upload, download, file management, sharing, content analysis, image processing, visual similar search, archive download, and mountapp installation or mounting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to operate Alibaba Cloud PDS files and spaces through documented CLI workflows. It supports common cloud-drive tasks such as locating files, transferring files, managing metadata, creating controlled share links, analyzing PDS-hosted content, processing images, and mounting PDS as a local disk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential or data exposure during setup and share-link workflows.

Mitigation: Use least-privilege PDS-only credentials, avoid putting secrets in command lines, and require passwords, expiration dates, and login restrictions before creating share links.

Risk: Mountapp installation can introduce a privileged persistent system change.

Mitigation: Review installation steps before use, prefer verified package-manager installs, verify AK authentication is configured, and require explicit confirmation before stopping or uninstalling mountapp.

Risk: The skill can reach beyond its stated PDS scope if agents improvise unsupported commands.

Mitigation: Limit execution to documented PDS commands and parameters, verify target drive and file identifiers before side effects, and stop on unsupported operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-pds-intelligent-workspace)
- [PDS Archive Download Guide](references/archive-download.md)
- [Aliyun CLI Installation and Configuration Guide](references/cli-installation-guide.md)
- [PDS Aliyun CLI Configuration Guide](references/config.md)
- [PDS File Download Guide](references/download-file.md)
- [PDS Drive Concepts and API Reference](references/drive.md)
- [PDS File Management](references/file-management.md)
- [PDS Image Editing Guide](references/image-editing.md)
- [Mount App Installation Guide](references/mountapp.md)
- [PDS Document and Audio/Video Analysis](references/multianalysis-file.md)
- [RAM Permission Requirements](references/ram-policies.md)
- [Resolve Between Cloud Path and file_id](references/resolve-path.md)
- [PDS File Search](references/search-file.md)
- [File Sharing](references/share-link.md)
- [PDS File Upload Guide](references/upload-file.md)
- [PDS Visual Similar Search Guide](references/visual-similar-search.md)
- [Alibaba Cloud RAM AccessKey management](https://ram.console.aliyun.com/manage/ak)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and CLI result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local files only when the user explicitly requests file transfer, download, or saved output.]

## Skill Version(s):

0.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
