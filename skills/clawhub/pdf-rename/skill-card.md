## Description: <br>
Rename academic PDF papers to a standardized "[Year] [Venue] Title.pdf" format using an extract, verify, and rename workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[67available](https://clawhub.ai/user/67available) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers use this skill to organize folders of academic PDFs by extracting first-page text, verifying paper metadata, previewing proposed names, and optionally applying batch renames. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow reads text from the first pages of every PDF in the selected folder and stores extracted text in manifest files. <br>
Mitigation: Run it only on intended folders and avoid optional LLM parsing for private or unpublished PDFs unless the local LLM gateway and its data handling are trusted. <br>
Risk: The execute stage can rename files in bulk when run with --execute. <br>
Mitigation: Run extract and preview first, review verified metadata before execution, and rely on the backup directory created during execution. <br>
Risk: The package includes leftover helper scripts and document/path state that may not be needed for normal use. <br>
Mitigation: Use the documented extract, apply_verified, and execute pipeline, and avoid undocumented helper scripts unless they have been reviewed. <br>


## Reference(s): <br>
- [Manifest Schema](references/manifest_spec.md) <br>
- [Standard Venue Abbreviations](references/venue_abbrev.md) <br>
- [Common Mistakes and Anti-patterns](references/anti_patterns.md) <br>
- [ClawHub skill page](https://clawhub.ai/67available/skills/pdf-rename) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with bash commands and JSON metadata examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates manifest JSON files and can rename PDF files after preview and verification.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
