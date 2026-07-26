## Description: <br>
Helps an agent batch rename local files with prefixes, suffixes, find-and-replace, extension filtering, sequence numbering, and dry-run previews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and power users use this skill to organize batches of screenshots, photos, documents, and project files by applying consistent local filename rules before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch renaming can unintentionally change many filenames in a selected folder. <br>
Mitigation: Run with --dry-run first, test on a small folder or backup, and confirm the rename plan before executing. <br>
Risk: The documented regex replacement behavior is not implemented as regex in this version. <br>
Mitigation: Treat replacement as literal find-and-replace unless the script is updated and reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/cn-file-batch-rename) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local Python standard-library script; dry-run previews are available before applying filename changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
