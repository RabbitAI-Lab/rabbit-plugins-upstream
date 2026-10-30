## Description:

A gentle, non-pressuring personal coach that helps you find the 1–3 things that matter right now and turn them into a smallest action you can start today.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External users use this personal coaching skill to clarify their current priorities, choose a small action for today, and review routines over time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved local history is readable, and deletion has no built-in undo.

Mitigation: Save only information the user explicitly approves and back up important records before deletion.

Risk: A generic greeting may reopen previously saved priorities.

Mitigation: Confirm the user wants to resume before acting on saved priorities.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Cold-start flow](references/cold-start.md)
- [Daily flows](references/daily-flows.md)
- [Memory schema](references/memory-schema.md)
- [Priority review](references/review.md)
- [State and coaching flows](references/states.md)
- [Conversation routing](references/router.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown coaching cards and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [At most three priorities and one small next action; optional local JSON history is saved only with user consent.]

## Skill Version(s):

0.3.6 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
