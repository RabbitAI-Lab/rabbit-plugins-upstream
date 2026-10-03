## Description:

Searches public uNotes course materials and answers study questions with named, linked document sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to find public course notes, exams, assignments, and lab reports, then get source-linked answers to study questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting uNotes grants access through OAuth to search the shared public library and read documents by ID.

Mitigation: Review requested uNotes access before connecting; provide document IDs only when needed.

Risk: Search results may contain other students' public uploads rather than the user's own documents.

Mitigation: Identify each source and clarify that search covers the shared public library when relevant.

Risk: Document content is capped at 12,000 characters and may end mid-sentence.

Mitigation: Disclose when an answer covers only the available first portion of a document.

## Reference(s):

- [uNotes: Researching Course Material on ClawHub](https://clawhub.ai/bsalaeddin/skills/unotes-researching-course-material)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown with document names and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only responses; document text may be truncated after 12,000 characters.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
