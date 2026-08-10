## Description:

Provides agent guidance for Alibaba Cloud PDS file operations, including search, upload, download, rename, move, copy, folder creation, metadata updates, share links, archive download, file analysis, image editing, and visual similar search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when they need an agent to operate files and spaces in Alibaba Cloud PDS through documented CLI workflows. It is intended for concrete PDS actions such as finding, moving, downloading, sharing, analyzing, or processing cloud files rather than general product Q&A.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide cloud-file mutations such as overwrites, renames, moves, copies, share-link creation, and archive/download actions.

Mitigation: Require a unique target and user confirmation before side-effecting operations, especially overwrites and ambiguous file matches.

Risk: Share links can expose PDS files, including links without expiration or weak access controls.

Mitigation: Prefer expiring, password-protected, or login-required shares and avoid exposing phone, email, or long-lived credentials in shared sessions.

Risk: Mount app installation, startup enablement, and uninstall workflows affect the local host and can introduce persistent drive mounting behavior.

Mitigation: Allow mount app installation, startup persistence, or uninstall actions only after the user explicitly requests that host-level behavior.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [PDS Aliyun CLI Configuration Guide](artifact/references/config.md)
- [PDS Drive Concepts and API Reference](artifact/references/drive.md)
- [PDS File Management](artifact/references/file-management.md)
- [PDS File Search](artifact/references/search-file.md)
- [PDS File Upload Guide](artifact/references/upload-file.md)
- [PDS File Download Guide](artifact/references/download-file.md)
- [PDS Archive Download Guide](artifact/references/archive-download.md)
- [File Sharing](artifact/references/share-link.md)
- [PDS Image Editing Guide](artifact/references/image-editing.md)
- [PDS Visual Similar Search Guide](artifact/references/visual-similar-search.md)
- [PDS Multianalysis File Guide](artifact/references/multianalysis-file.md)
- [RAM Permission Policies](artifact/references/ram-policies.md)
- [Resolve Path Guide](artifact/references/resolve-path.md)
- [Mount App Guide](artifact/references/mountapp.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown guidance with inline shell commands and CLI result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or modify PDS cloud files and may save downloaded files or archives locally when explicitly requested.]

## Skill Version(s):

0.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
