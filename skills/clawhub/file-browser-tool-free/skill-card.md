## Description: <br>
文件浏览器(免费版) helps an agent browse directories, inspect text files, run basic searches, and perform simple local file operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent list directories, preview text files, search file names or contents, and manage individual files in a local workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete, move, overwrite, or create local files when paired with agent execution tools. <br>
Mitigation: Require explicit target paths and explicit confirmation before delete, move, overwrite, or cross-filesystem operations. <br>
Risk: The skill may operate outside the intended project or workspace if paths are not constrained. <br>
Mitigation: Limit use to an intended workspace and reject broad or ambiguous paths before running file operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-browser-tool-free) <br>
- [Detailed reference](references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with command examples, Python snippets, and structured JSON-style operation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include file paths, command output, operation status, execution logs, and error messages.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
