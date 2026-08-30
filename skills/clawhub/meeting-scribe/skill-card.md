## Description:

Turn a meeting transcript into structured meeting memory: a dated meeting note, one appended mention line per tracked entity named in the transcript, and a recap email drafted for review but never sent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skillsandagentsco](https://clawhub.ai/user/skillsandagentsco)

### License/Terms of Use:

MIT-0

## Use Case:

Teams use this skill after meetings to turn transcripts into durable meeting memory across local people, organization, and meeting files. It is intended for users who want quote-grounded mention timelines, proposed new entities, ambiguity flags, follow-ups, and a human-reviewed recap draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads meeting transcripts and entity files and appends local meeting history, which may include sensitive business context.

Mitigation: Run it only against the intended transcript and entity folder, and review generated notes, mention lines, and recap drafts before using them.

Risk: A transcript or existing entity file may contain text that attempts to steer the agent.

Mitigation: Treat transcript and entity content as data, flag embedded instruction-like text in the run output, and do not store flagged instruction text in written files.

Risk: Incorrect identity matching could attach meeting history to the wrong person, organization, or meeting.

Mitigation: Use file-first exact and alias matching, propose unmatched entities for confirmation, and write nothing for ambiguous matches until a human resolves them.

Risk: A recap email could be mistaken for an authorized send action.

Mitigation: Keep the recap as draft text only; the skill has no mail-sending step and requires human review before any external use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/skillsandagentsco/skills/meeting-scribe)
- [Skills & Agents catalog page](https://skillsandagents.co/skills/meeting-scribe/)
- [USV Meeting Scribe inspiration](https://blog.usv.com/meet-the-agents)
- [Mention proposal shape](artifact/references/mention-proposal.md)
- [Sample transcript](artifact/references/sample-transcript.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown files, appended markdown mention lines, drafted email text, and optional YAML configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in the transcript and existing entity files; recap email is draft-only and never sent.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
