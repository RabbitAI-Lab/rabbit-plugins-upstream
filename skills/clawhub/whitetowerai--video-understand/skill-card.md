## Description:

Use when a video project needs reusable media metadata, word-level transcription, objective speech analysis, or evidence-backed semantic understanding before optional editing skills run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitetowerai](https://clawhub.ai/user/whitetowerai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation agents use this skill to initialize a video project, extract media metadata and word-level transcripts, analyze objective speech signals, and author factual semantic evidence before downstream edit skills run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes rendering utilities beyond the stated understanding workflow, including behavior that can create final media and update render verification state.

Mitigation: Review installed files before use and run only the understanding workflow unless rendering behavior is explicitly intended.

Risk: Executable utilities can overwrite project outputs when invoked.

Mitigation: Run the skill in a project-local workspace, keep source media backed up, and inspect generated outputs and project state before accepting them.

## Reference(s):

- [Project Schema V1](artifact/reference/project-schema.md)
- [Timeline Schema V1](artifact/reference/timeline-schema.md)
- [Understanding Schema V1](artifact/reference/understanding-schema.md)
- [Understanding Example](artifact/examples/understanding.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON file contracts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces project-local JSON, SRT, Markdown summary, contact sheet, and validated timeline and understanding artifacts.]

## Skill Version(s):

1.0.5 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
