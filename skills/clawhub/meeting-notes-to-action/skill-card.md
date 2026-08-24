## Description:

Turn raw meeting notes or transcripts into structured action: decisions log, action items with owner and deadline, open questions, and a distributable summary email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Employees, team leads, project coordinators, executive assistants, consultants, and other meeting participants use this skill to convert meeting notes or transcripts into decisions, action items, open questions, Markdown minutes, JSON records, and follow-up email drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated minutes or email drafts may contain incorrect assignments, deadlines, or summaries from low-confidence extraction.

Mitigation: Review confidence flags, unassigned items, relative dates, and per-owner sections before distributing minutes or email drafts.

Risk: Meeting notes can contain confidential business information.

Mitigation: Run the local script only on notes the user is comfortable processing and review generated artifacts before sharing them.

## Reference(s):

- [Extraction Patterns & Confidence Scoring](references/extraction-patterns.md)
- [Minutes & Email Templates](references/minutes-templates.md)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/meeting-notes-to-action)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus generated JSON, Markdown minutes, terminal digest, and summary email draft outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated action items include owners, deadlines, confidence flags, source lines, duplicate counts, and carryover status when previous meeting JSON is supplied.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
