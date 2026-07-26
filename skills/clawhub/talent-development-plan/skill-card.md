## Description: <br>
Generates vocational education talent development plans by combining occupational analysis, teaching standards, national public-course requirements, and built-in secondary or higher vocational templates into Markdown and DOCX-ready program documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Vocational college program leads, department heads, and curriculum designers use this skill to draft professional talent development plans from program details, teaching standards, and occupational analysis reports. It supports secondary vocational, higher vocational, and integrated pathways with structured curriculum, teaching schedule, compliance, and DOCX formatting guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic teaching-standard retrieval may fetch remote PDF content when that workflow is enabled. <br>
Mitigation: Confirm whether remote retrieval is acceptable before use, or require uploaded/local teaching-standard files only. <br>
Risk: Intermediate and final Markdown, DOCX, and image files may contain user-provided education materials. <br>
Mitigation: Run the workflow in a non-sensitive working folder and review generated files before sharing or storing them. <br>
Risk: Generated plans may be used for curriculum decisions and can contain omissions or mismatches if source standards or occupational reports are incomplete. <br>
Mitigation: Have qualified program staff review the generated plan against official teaching standards and the built-in self-check guidance before institutional adoption. <br>


## Reference(s): <br>
- [Course Objective Generation Rules](artifact/references/course-objective-generation.md) <br>
- [Error Recovery Guide](artifact/references/error-recovery.md) <br>
- [National Standards Reference](artifact/references/national-standards.md) <br>
- [Self-Check List](artifact/references/self-check-list.md) <br>
- [Teaching Schedule Rules](artifact/references/teaching-schedule-rules.md) <br>
- [Template Chapters](artifact/references/template-chapters.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/flyboat403/skills/talent-development-plan) <br>
- [Server-Resolved Source Repository](https://github.com/flyboat403/talent-development-plan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and DOCX-ready document content with supporting shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates intermediate and final document files, may generate a curriculum architecture PNG, and relies on user review before institutional use.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
