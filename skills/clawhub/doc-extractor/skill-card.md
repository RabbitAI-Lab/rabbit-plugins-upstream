## Description: <br>
Extract text from PDF, DOCX, and TXT with encoding detection and page/paragraph structure. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, RAG builders, researchers, and data engineers use this skill to extract readable text from individual documents or document folders for search, indexing, and downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Batch extraction reads local document folders and may write extracted text to an output directory. <br>
Mitigation: Run batch mode only on intended document folders and review extracted text destinations before sharing or indexing outputs. <br>
Risk: The CI verification helper executes local package checks and should not be used blindly on untrusted code. <br>
Mitigation: Use the CI verification helper only with trusted packages or inside a sandbox. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/itspremkumar/skills/doc-extractor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with command examples and extracted plain text files or console text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PDF extraction requires the optional pymupdf dependency; single-file extraction can print a preview or write full text to an output file, and batch mode can write per-document text files.] <br>

## Skill Version(s): <br>
2.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
