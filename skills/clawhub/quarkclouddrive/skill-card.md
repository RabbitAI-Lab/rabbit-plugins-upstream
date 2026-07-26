## Description: <br>
Quark Drive Skill helps agents authenticate with Quark Drive and upload, download, share, transfer, search, organize media, and use file summary or Q&A features. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[quarkdrive](https://clawhub.ai/user/quarkdrive) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to operate a Quark Drive account from conversation: manage cloud files, save shared links, find files, organize personal media, and ask summary or Q&A questions over stored files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer may change the local Node.js installation and download updated skill code or instructions from a remote service. <br>
Mitigation: Run it only in an environment where package changes and remote self-updates are acceptable, and review the publisher and release before installation. <br>
Risk: Commands may send original user prompts for service-quality tracking. <br>
Mitigation: Avoid using the skill with sensitive prompts unless sharing that text with the service is acceptable. <br>
Risk: Reading cloud files may persist copies on local storage. <br>
Mitigation: Use the skill in a workspace where local file copies are expected and clean up downloaded files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/quarkdrive/skills/quarkclouddrive) <br>
- [Publisher profile](https://clawhub.ai/user/quarkdrive) <br>
- [Quark Drive](https://pan.quark.cn) <br>
- [Authorization and account management](references/auth.md) <br>
- [File search](references/file-search.md) <br>
- [File upload](references/file-upload.md) <br>
- [File sharing](references/file-share.md) <br>
- [Album organization](references/file-organize.md) <br>
- [Assistant capabilities](references/assistant.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI command results may include NDJSON, links, and local file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a Quark Drive authorization flow before account-specific operations.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
