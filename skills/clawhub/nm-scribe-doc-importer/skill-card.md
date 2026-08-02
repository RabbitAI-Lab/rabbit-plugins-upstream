## Description: <br>
Converts external documents (PDF, DOCX, PPTX, XLSX, HTML) into editable markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to convert user-provided PDF, DOCX, PPTX, XLSX, or HTML files into editable markdown for project documentation, rewriting, or remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External documents may contain misleading instructions or conversion artifacts. <br>
Mitigation: Confirm the source and output path, sanitize external content, and review converted content before reuse. <br>
Risk: Unsupported or lossy conversions can omit or garble source content. <br>
Mitigation: Tell the user when a format is unsupported and mark unclear converted sections for review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-doc-importer) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, files, guidance] <br>
**Output Format:** [Markdown file plus concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May mark unclear conversion artifacts for review and may offer an optional documentation remediation handoff.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
