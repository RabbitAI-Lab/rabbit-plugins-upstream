## Description:

Track job applications, contacts, deadlines, and follow-up reminders in a local SQLite database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mehulupase01](https://clawhub.ai/user/mehulupase01)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers and career-management agents use this skill to log applications, recruiter contacts, deadlines, follow-up reminders, status changes, and pipeline summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job applications, recruiter contact details, deadlines, and notes are stored locally in a plaintext SQLite database.

Mitigation: Store only necessary job-search details, keep the skill directory on a trusted machine with appropriate filesystem permissions, and avoid secrets, government identifiers, passwords, tokens, or highly confidential interview details in notes.

Risk: Incomplete or inferred application details could create inaccurate records.

Mitigation: Confirm required fields and tentative dates with the user before writing records, and keep recruiter notes factual.

## Reference(s):

- [Status Guide](references/status-guide.md)
- [Project homepage](https://github.com/Mehulupase01/openclaw-skill-suite/tree/main/skills/job-tracker)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes job application data to a local SQLite database under .runtime/job-tracker.db.]

## Skill Version(s):

0.1.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
