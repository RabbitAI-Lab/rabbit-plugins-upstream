## Description: <br>
A batch file-processing toolbox for organizing files, converting formats, renaming files, compressing and extracting archives, detecting duplicates, and generating folder reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cx75227-ops](https://clawhub.ai/user/cx75227-ops) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and users who manage folders at scale use this skill to plan or perform batch file organization, conversion, renaming, archive handling, duplicate detection, and folder reporting tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk file operations may rename, move, convert, compress, or deduplicate files in ways that are hard to undo. <br>
Mitigation: Use the skill only on intentionally selected folders, keep backups for important data, and request a dry run or preview before allowing bulk changes. <br>
Risk: The security summary notes a safety documentation gap for a file-management skill with file-changing capabilities. <br>
Mitigation: Review the planned operations and scan the skill before deployment, especially for workflows that modify many files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cx75227-ops/skills/file-processor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with actionable steps and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute bulk file operations; users should review planned changes before running destructive actions.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
