## Description: <br>
Qms Form Builder helps field inspectors, test staff, and equipment checkers create printable blank quality-management forms for inspection records, test reports, and equipment checklists as Excel or Word templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External quality teams, field inspectors, test engineers, and equipment maintainers use this skill to create standardized blank forms for recording inspection, test, or checklist data. Users remain responsible for supplying and confirming technical standards, sampling plans, and project-specific requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package references generation scripts and reference files that are not present in the artifact, so the skill may not work as described without additional files. <br>
Mitigation: Confirm the required script and reference files are available and test Excel and Word generation before relying on the skill in a workflow. <br>
Risk: Generated quality forms can carry incorrect inspection standards, sampling plans, or acceptance criteria if the user supplies incomplete requirements. <br>
Mitigation: Have qualified quality staff provide and review inspection items, standards, sampling plans, and any fields marked for enterprise completion before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-qms-form-builder) <br>
- [Server-Resolved Source Repository](https://github.com/duding-engicool/skill-qms-form-builder) <br>
- [Packaged Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Excel (.xlsx) and Word (.docx) templates with concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates blank, printable quality-record templates in the user's current working directory; incomplete standards or sampling details should remain marked for enterprise completion.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; packaged SKILL.md frontmatter says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
