## Description: <br>
Create, inspect, and edit Microsoft Word documents and DOCX files with reliable styles, numbering, tracked changes, tables, sections, and compatibility checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, editors, and document automation users use this skill to create, inspect, or preserve DOCX files when formatting, tracked changes, comments, fields, tables, numbering, templates, or round-trip compatibility matter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Word documents may contain sensitive content in tracked changes, comments, deleted text, fields, or metadata. <br>
Mitigation: Use the skill only on documents you are comfortable sharing with the agent, and inspect revisions, comments, deleted text, and metadata before delivery. <br>
Risk: DOCX edits can break formatting, numbering, references, or layout when opened in Word, LibreOffice, Google Docs, or conversion tools. <br>
Mitigation: Prefer style- and OOXML-aware edits, make minimal review-preserving changes, and perform round-trip compatibility checks when layout matters. <br>
Risk: Macro-bearing or legacy Word files can carry higher compatibility and security risk than normal DOCX files. <br>
Mitigation: Treat DOCM files as macro-bearing and higher risk, and convert or inspect legacy DOC inputs before relying on modern DOCX assumptions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/xiaomolong-word-docx) <br>
- [Skill homepage](https://clawic.com/skills/word-docx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file, command, code, and DOCX workflow recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend OOXML-aware inspection, document conversion, compatibility checks, and review-preserving edits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
