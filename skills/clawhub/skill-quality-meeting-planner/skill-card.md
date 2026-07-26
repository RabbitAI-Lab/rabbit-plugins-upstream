## Description: <br>
Parses user-provided quality data and work issues, checks required meeting details, confirms an outline, and generates a structured Word document for quality weekly meeting planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Quality, QA, and delivery teams use this skill to turn quality metrics, defect notes, tables, and work issues into a confirmed weekly meeting outline and a formatted Word planning document. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided quality meeting data may contain sensitive business information. <br>
Mitigation: Process only data that is appropriate for the agent environment and follow the organization's normal handling rules before sharing generated meeting materials. <br>
Risk: The document generation script writes a Word file to the requested output path. <br>
Mitigation: Choose the output path intentionally and review the generated document before distributing it. <br>


## Reference(s): <br>
- [Meeting Schema](references/meeting-schema.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-quality-meeting-planner) <br>
- [Publisher Profile](https://clawhub.ai/user/duding-engicool) <br>
- [Server-Resolved Source Repository](https://github.com/duding-engicool/skill-quality-meeting-planner) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown meeting outline plus JSON input for a local DOCX generation script; final artifact is a Word document.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation of the outline before document generation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter states 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
