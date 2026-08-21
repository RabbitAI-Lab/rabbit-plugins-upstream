## Description:

Capture and promote durable agent learnings in QMD-indexed Markdown when reflection or reusable memory is requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shakerg](https://clawhub.ai/user/shakerg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to capture intentional reflections, repeated failures, corrections, and recurring practices as reviewable Markdown knowledge while respecting approval, privacy, and workspace conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed learning could persist secrets, personal data, confidential content, or raw prompt material.

Mitigation: Redact sensitive material before proposing or writing a learning, and require explicit approval for sensitive, personal, or organization-confidential content.

Risk: A learning could be written to the wrong destination or change authoritative guidance without the right review.

Mitigation: Search existing Markdown first, propose the destination and classification, and require explicit approval before creating durable files or editing authoritative guidance.

Risk: QMD indexing could include paths the workspace owner did not intend to index.

Mitigation: Run QMD mutation commands only after approval, avoid adding collections or changing configuration casually, and index only paths the user intentionally chooses.

Risk: Unsupported or conflicting lessons could introduce misleading durable guidance.

Mitigation: Promote only concrete, recurring, non-duplicative lessons; preserve conflicts as needs-review instead of silently overwriting existing rules.

## Reference(s):

- [QMD Learning Loop ClawHub page](https://clawhub.ai/shakerg/skills/qmd-learning-loop)
- [QMD Learning Loop homepage](https://github.com/shakerg/qmd-learning-loop)
- [QMD project](https://github.com/tobi/qmd)
- [Destination Discovery](references/destination-discovery.md)
- [Evaluation Cases](references/evaluation-cases.md)
- [QMD Workflow](references/qmd-workflow.md)
- [Review Loop](references/review-loop.md)
- [Templates](references/templates.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional shell command snippets and approved file edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes occur only after explicit approval; QMD indexing commands are optional.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
