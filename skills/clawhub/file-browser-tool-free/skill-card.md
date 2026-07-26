## Description: <br>
文件浏览器(免费版) helps an agent browse directories, preview text files, search filenames and file contents, and perform basic local file operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and developers use this skill to inspect local directories, preview text files, search files, and perform basic copy, move, delete, rename, and directory-creation tasks through an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad local file actions, including delete, move, copy, overwrite, and cross-filesystem operations. <br>
Mitigation: Use explicit paths, keep backups, avoid sensitive directories, and require manual confirmation before destructive or recursive operations. <br>
Risk: Shell commands or file-management guidance may modify files reachable by the agent's local permissions. <br>
Mitigation: Review commands before execution and run the agent in the least-privileged workspace that still supports the task. <br>
Risk: Directory browsing, text preview, and search can expose sensitive local content. <br>
Mitigation: Limit searches to intended folders and avoid using the skill on directories containing secrets, credentials, or private data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-browser-tool-free) <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with shell commands, Python snippets, and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include file paths, status messages, execution logs, and local filesystem operation results.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
