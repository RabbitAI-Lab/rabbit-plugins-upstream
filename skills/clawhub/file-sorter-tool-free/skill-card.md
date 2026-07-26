## Description: <br>
视觉文件整理免费版 helps agents visually inspect local files, rename them, and move them into simple category folders for personal desktop or downloads cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals use this skill to preview and organize intentionally selected desktop or downloads folders by file content, especially invoices, contracts, documents, and images. It is best suited for lightweight personal filing where file moves and renames can be reviewed before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rename and move local files, and server security evidence flags scope and deletion inconsistencies. <br>
Mitigation: Run dry-run first, restrict execution to folders intentionally selected by the user, keep backups for important documents, and review proposed moves before applying them. <br>
Risk: Visual inspection of local documents may expose sensitive contents if routed through an unintended model or service. <br>
Mitigation: Use only approved local or default agent vision capabilities and avoid sending screenshots or document contents to unauthorized third-party APIs. <br>
Risk: Incorrect classification or renaming can make files harder to locate or associate with their original context. <br>
Mitigation: Preserve file extensions, keep unrecognized files under an unclassified prefix or folder, and verify renamed financial or work documents before relying on the results. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/file-sorter-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-style execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file rename and move operations, dry-run previews, category summaries, and execution logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
