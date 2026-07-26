## Description: <br>
Advanced filesystem operations for listing files, searching content, batch processing, and directory analysis with recursive search, file type filtering, size analysis, and batch operation examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[AmaoFx](https://clawhub.ai/user/AmaoFx) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to plan and perform local filesystem tasks such as listing directories, searching by file name or content, analyzing disk usage, and preparing batch file operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk delete, move, rename, or in-place replacement commands can change or remove local files. <br>
Mitigation: Preview the matched files, confirm target directories, use dry-run or interactive modes when available, and keep backups before approving commands. <br>
Risk: Optional command-line tools may require local installation. <br>
Mitigation: Install tools such as tree, fd, and ripgrep only through a package manager you trust. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/AmaoFx/filesystem) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes filesystem command examples for search, analysis, and batch operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
