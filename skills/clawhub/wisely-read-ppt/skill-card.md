## Description: <br>
Parses PPTX or PDF files page by page into structured DOCX analysis documents with page screenshots, editable text, and inline image descriptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sedey999](https://clawhub.ai/user/sedey999) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to convert PPTX or PDF decks into reviewed DOCX analysis drafts for content extraction, slide-by-slide reading, and editable report preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The parser may install unpinned Python packages automatically. <br>
Mitigation: Use an isolated virtual environment or container, preinstall dependencies yourself, and run the parser with --no-install. <br>
Risk: Input documents are exposed to local parsing, generated screenshots, extracted assets, and agent visual review. <br>
Mitigation: Process only documents you are comfortable retaining in the workspace and remove working assets when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/sedey999/skills/wisely-read-ppt) <br>
- [README](README.md) <br>
- [Subagent Workflow](reference/subagent-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [DOCX files with markdown-style inline image markers, local asset files, and a markdown task report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes PPTX and PDF inputs page by page; uses local screenshots, extracted images, and visual review before final delivery.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
