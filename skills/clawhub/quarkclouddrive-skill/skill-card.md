## Description: <br>
夸克网盘官方(Quark Drive)Skill，用于文件上传/下载（支持断点续传）、文件分享与转存、网盘文件搜索、相册整理、AI助手（文件总结与知识问答，支持万级文件）。当用户需要操作夸克网盘文件或进行身份验证时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hope0719](https://clawhub.ai/user/hope0719) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to operate Quark Drive accounts: authenticate, upload and read files, save shared links, search drive contents, organize photos and videos, share files, and summarize or answer questions over drive files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence reports bundled credential configuration. <br>
Mitigation: Remove the credential config or confirm it is harmless before installation, especially in sensitive environments. <br>
Risk: The skill performs self-install and update actions from a remote endpoint. <br>
Mitigation: Use a signed or platform-managed update path, or manually install only after trusting the update endpoint. <br>
Risk: Prompts, session IDs, and drive metadata may be sent for tracking. <br>
Mitigation: Use the skill only where that tracking is acceptable and avoid sending sensitive prompts unless explicitly approved. <br>
Risk: Cloud-drive operations can upload, save, share, organize, or uninstall user data and configuration. <br>
Mitigation: Require explicit confirmation for uploads, save-as operations, sharing, uninstall, and other sensitive file actions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hope0719/skills/quarkclouddrive-skill) <br>
- [Quark Drive](https://pan.quark.cn) <br>
- [assistant.md](references/assistant.md) <br>
- [auth.md](references/auth.md) <br>
- [file-ops.md](references/file-ops.md) <br>
- [file-organize.md](references/file-organize.md) <br>
- [file-read.md](references/file-read.md) <br>
- [file-saveas.md](references/file-saveas.md) <br>
- [file-search.md](references/file-search.md) <br>
- [file-share.md](references/file-share.md) <br>
- [file-upload.md](references/file-upload.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell command examples and NDJSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and Quark Drive authorization; CLI operations may create, upload, read, share, organize, or modify cloud-drive files.] <br>

## Skill Version(s): <br>
1.0.10 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
