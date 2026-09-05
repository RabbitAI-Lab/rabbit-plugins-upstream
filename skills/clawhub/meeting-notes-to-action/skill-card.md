## Description:

Turn raw meeting notes or transcripts into structured action: decisions log, action items with owner and deadline, open questions, and a distributable summary email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, team leads, PMs, project coordinators, executive assistants, consultants, and developers use this skill to convert meeting notes, chat exports, or transcript text into decisions, action items, open questions, carryover tracking, minutes, and follow-up email drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes may contain sensitive business, personnel, or customer information.

Mitigation: Use the skill only on notes suitable for local processing and treat generated summaries, JSON, minutes, and email drafts as sensitive until reviewed.

Risk: Deterministic extraction can misread ambiguous commitments, weak language, relative dates, or question-form delegations.

Mitigation: Review low-confidence items, unassigned owners, accepted delegations, and resolved dates before relying on the output or distributing an email draft.

Risk: Carryover and per-owner task lists can become misleading if stale or completed items are not checked.

Mitigation: Validate carryover items against the current meeting record and confirm per-owner sections before sending follow-up notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/meeting-notes-to-action)
- [Server-resolved GitHub provenance](https://github.com/voronindenis5/meeting-notes-to-action)
- [Extraction patterns](references/extraction-patterns.md)
- [Minutes templates](references/minutes-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Terminal text, JSON records, Markdown minutes, and Markdown email drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-selected local meeting note files and can write user-selected JSON, minutes, and email output files.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
