## Description:

A gentle, non-pressuring personal coach that helps users identify the 1-3 things that matter right now and turn the top priority into a small action they can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill as a personal priority coach to sort through overload, choose the most important 1-3 priorities, and produce a low-pressure next action for today. It is not intended for team project management, bidirectional task synchronization, or making major life decisions on the user's behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved local coaching records may contain sensitive priorities, reflections, or raw answers.

Mitigation: Save records only after explicit user consent, avoid storing rawAnswers unless separately approved, and remind users that records can be exported or deleted.

Risk: Export, migration, and bulk delete commands can expose or remove personal coaching history.

Mitigation: Confirm the requested action and target records before running export, migrate, delete, or session-delete commands.

Risk: A user may present self-harm, violence, or severe medical or mental-health crisis signals that are outside priority coaching.

Mitigation: Pause normal priority coaching and encourage the user to contact local emergency support, a trusted person, or qualified professional help.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Cold-start questions and summarization rules](references/cold-start.md)
- [Copy tone guidance](references/copy-tone.md)
- [Daily flows](references/daily-flows.md)
- [Memory schema](references/memory-schema.md)
- [Mainline review and resume flow](references/review.md)
- [State router](references/router.md)
- [State dialogue scripts](references/states.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown coaching responses with structured cards and occasional local record-management shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save, export, summarize, or delete local priority-coaching records only when the user explicitly agrees.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
