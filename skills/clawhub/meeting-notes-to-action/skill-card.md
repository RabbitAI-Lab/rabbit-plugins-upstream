## Description:

Turn raw meeting notes or transcripts into structured action: decisions log, action items with owner and deadline, open questions, and a distributable summary email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Employees and external workplace users use this skill to convert meeting notes, chat exports, or transcript text into decisions, action items, open questions, Markdown minutes, JSON records, and follow-up email drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting notes and extracted action items may contain confidential business or personnel information.

Mitigation: Review generated minutes and email drafts before sharing, and choose output locations carefully.

Risk: The skill reads notes, prior JSON files, and selected output paths from the local filesystem.

Mitigation: Scope agent file access to the intended notes, prior JSON files, and selected output paths.

Risk: Deterministic extraction can misread ambiguous commitments, deadlines, owners, or question-style delegations.

Mitigation: Review confidence flags, unresolved owners, relative dates, and email drafts before distribution.

## Reference(s):

- [Server-resolved source repository](https://github.com/voronindenis5/meeting-notes-to-action)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/meeting-notes-to-action)
- [Extraction Patterns & Confidence Scoring](references/extraction-patterns.md)
- [Minutes & Email Templates](references/minutes-templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Terminal digest, JSON records, Markdown minutes, and summary email draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional file outputs are written only to user-selected paths; relative dates should be resolved with an explicit meeting date.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
