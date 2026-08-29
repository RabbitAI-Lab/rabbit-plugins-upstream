## Description:

Inspect, edit, and export CorelDRAW CDR files via CorelDRAW automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stanestane](https://clawhub.ai/user/stanestane)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and design automation users use this skill to inspect CorelDRAW CDR document structure, create previews, export selected artwork, and apply conservative copy-first edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: In-place edits can overwrite or damage CDR files.

Mitigation: Use copy-first output paths, inspect previews before and after edits, and use --in-place only after making a backup.

Risk: The agent can open and read or write the CDR files the user specifies through CorelDRAW.

Mitigation: Install only when that file access is acceptable and limit runs to intended input and output paths.

Risk: Shape indexes are document-order dependent and can change after grouping, ungrouping, deleting, or duplicating objects.

Mitigation: Re-inspect the edited copy before applying follow-up operations or reporting final results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stanestane/skills/coreldraw-editor)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown with inline shell commands, JSON operation plans, and generated files such as previews, exports, manifests, or edited CDR copies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows, installed CorelDRAW, and pywin32; ImageMagick is optional for validation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
