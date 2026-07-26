## Description: <br>
Tracks China national standard updates for a selected ICS category, compares the current official listing with local metadata, reports additions, removals, and status changes, and can optionally download available PDF files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sereinone](https://clawhub.ai/user/sereinone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, standards managers, and compliance teams use this skill to monitor GB/GB/T standards for an ICS category, generate update reports, and keep local standards metadata or downloaded PDFs current. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates or updates JSON metadata, reports, snapshots, and optional PDF files in the selected directory. <br>
Mitigation: Use a dedicated working directory and review generated files before relying on them for standards management decisions. <br>
Risk: Optional downloads may contact openstd.samr.gov.cn repeatedly. <br>
Mitigation: Confirm download intent with the user and rely on the built-in pauses between download batches. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/sereinone/skills/national-standard-monitor-skill) <br>
- [China national standards public service platform](https://openstd.samr.gov.cn/bzgk/gb) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, Files] <br>
**Output Format:** [Markdown summaries with inline shell commands; generated report and metadata files are JSON, with optional PDF downloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and a user-selected working directory for JSON metadata, reports, snapshots, and optional PDF files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
