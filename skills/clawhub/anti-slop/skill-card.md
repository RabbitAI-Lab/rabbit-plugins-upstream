## Description:

Detects and removes formulaic AI-style writing and common AI-generated code anti-patterns through a deliberate editing pass and optional density scanner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and engineers use this skill as a second-pass editor for substantial prose or non-trivial code. It helps identify generic AI-style phrasing, excess formatting, sycophantic openers, over-engineering, swallowed errors, hallucinated APIs, and similar patterns before final delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may review sensitive drafts or code during an editing pass.

Mitigation: Use normal care with sensitive documents, and run the optional scanner only on files that are intended for analysis.

Risk: Diagnostic scanner findings or style checklist items may be over-applied and remove useful wording, formatting, or code structure.

Mitigation: Treat findings as advisory, preserve intentional choices, and confirm edits still preserve meaning, correctness, and project conventions.

## Reference(s):

- [Prose Tells: The Full Reference](references/prose-tells.md)
- [Code Slop: The Full Reference](references/code-slop.md)
- [Self-Edit Checklist](references/self-edit-checklist.md)
- [Research Notes](references/research-notes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown or plain text edits and recommendations, with optional JSON scanner output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional scanner output is diagnostic and should not be treated as a mandatory rewrite instruction.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
