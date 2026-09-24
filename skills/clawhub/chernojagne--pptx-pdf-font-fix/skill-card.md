## Description:

Fixes PowerPoint font embedding issues in PDF export by patching text transparency in PPTX files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chernojagne](https://clawhub.ai/user/chernojagne)

### License/Terms of Use:


## Use Case:

Developers and document automation agents use this skill to patch trusted PPTX files when PowerPoint PDF export substitutes wrong/default fonts despite font embedding settings. The patched presentation is opened in PowerPoint desktop for PDF export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted or unusually large PPTX files can cause resource exhaustion during local processing.

Mitigation: Process only trusted PPTX files or run in a constrained environment with file-size and runtime limits.

Risk: Overwriting the original presentation can make recovery harder if the patched file does not open as expected.

Mitigation: Choose an explicit output path, keep the original unchanged, and verify the patched presentation opens correctly before using it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chernojagne/skills/pptx-pdf-font-fix)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Patched PPTX file plus Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PowerPoint desktop for final PDF export; server-side converters are not expected to reproduce the workaround.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
