## Description:

Priority Coach helps users turn overwhelm into one to three current priorities, choose a small action they can start today, and use low-pressure daily check-ins when they are stuck, overloaded, starting, or winding down.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this coaching skill to clarify personal priorities, reduce overcommitment, and convert the most important current focus into a small, concrete next action. It is especially suited for sessions about feeling busy but unfocused, planning today lightly, starting a first step, wrapping up the day, checking recurring habits, or switching to an overwhelmed mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional local priority records can retain sensitive personal context if the user chooses to save them.

Mitigation: Save records only after explicit user consent, prefer result cards over raw answers, and avoid saving sensitive raw answers unless the user explicitly wants them retained locally.

Risk: Record export, delete, and migration commands affect local priority-coach data.

Mitigation: Run save, export, delete, or migrate commands only when the user intends that action, and use the path or list command first when the user needs to inspect what data exists.

Risk: High-risk self-harm, violence, severe medical, or mental-health crisis statements are outside ordinary priority coaching.

Mitigation: Suspend normal priority coaching for those cases and direct the user toward trusted people, local emergency support, or professional help.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/priority-coach)
- [Router rules](references/router.md)
- [State scripts](references/states.md)
- [Cold start rules](references/cold-start.md)
- [Daily flows](references/daily-flows.md)
- [Memory schema](references/memory-schema.md)
- [Copy tone](references/copy-tone.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown coaching responses with structured priority, action, wrap-up, and low-burden cards; optional shell commands for local record management.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Limits normal coaching output to at most three priorities and one smallest next action; local records are saved only after explicit user consent.]

## Skill Version(s):

0.2.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
