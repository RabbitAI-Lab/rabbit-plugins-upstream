## Description: <br>
Compresses large PDF batches with Ghostscript first and PyMuPDF fallback, using size thresholds and DPI reduction to reduce file sizes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sereinone](https://clawhub.ai/user/sereinone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to find PDFs above a size threshold, compress them in batches, and generate compression logs and reports on macOS or Linux. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can permanently replace many PDFs with lossy compressed versions. <br>
Mitigation: Run it first on a copied test directory, keep backups of originals, and avoid using it on legal, archival, financial, or only-copy documents unless overwrite controls are added. <br>
Risk: PyMuPDF fallback may render pages into image-based PDFs, which can reduce quality and affect searchable text or OCR expectations. <br>
Mitigation: Verify whether searchable text or OCR matters for the target PDFs and inspect sample outputs before batch execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sereinone/skills/pdf-batch-compress) <br>
- [Project homepage](https://github.com/weidong/pdf-batch-compress) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and script references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce terminal logs and compression reports when the referenced scripts are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
