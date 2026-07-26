## Description: <br>
Help macOS users work with WPS Office more reliably when WPS is explicitly part of the document workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and document-workflow agents use this skill to prepare, convert, review, export, and troubleshoot files that will be opened or checked in WPS Office on macOS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Running the helper on documents may invoke uvx to run the MarkItDown converter. <br>
Mitigation: Review the conversion command before execution and use trusted local tooling for private or sensitive documents. <br>
Risk: The helper writes to the output path supplied by the user. <br>
Mitigation: Use copies or new output filenames for important documents rather than overwriting originals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/legionspace-hackathon/skills/wps-macos-helper) <br>
- [Workflow](references/workflow.md) <br>
- [Compatibility](references/compatibility.md) <br>
- [Export and Format](references/export-and-format.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Case Studies](references/case-studies.md) <br>
- [Release Checklist](references/release-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with optional shell commands and workflow-note files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper writes only to an explicitly supplied output path; document conversion depends on uvx and MarkItDown availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
