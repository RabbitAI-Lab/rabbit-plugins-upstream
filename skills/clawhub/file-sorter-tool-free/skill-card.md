## Description: <br>
视觉文件整理免费版 helps an agent inspect, rename, and organize local desktop or downloads files by content using visual recognition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users can use this skill to organize personal Downloads or Desktop folders, classify invoices, contracts, images, and other documents, and generate safer names and destination folders before applying file moves. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad local file access and can inspect, rename, and move files in selected folders. <br>
Mitigation: Run a dry-run first, target narrow folders, and keep backups or filesystem snapshots for important documents. <br>
Risk: Visual recognition may expose sensitive file contents depending on the agent and model environment. <br>
Mitigation: Avoid broad folders containing private records unless the user understands where vision processing happens and has approved it. <br>
Risk: The free edition does not provide operation history or rollback. <br>
Mitigation: Review planned file names and destinations before execution and preserve originals when recovery matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/file-sorter-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell command examples and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces proposed organization steps, command examples, status summaries, and execution logs; users should review dry-run results before moving files.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
