## Description:

Stoic Coach guides users through structured Stoic practice, daily reflection routines, local journaling, progress review, and quote-based prompts when the user explicitly asks for Stoic coaching or practice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill for guided Stoic exercises, lightweight morning and evening routines, local practice tracking, and reflection over personal patterns. It is intended as a philosophy practice aid, not mental health treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal reflections, mood scores, routines, and insights may be sensitive and are stored locally in plaintext.

Mitigation: Use a private or encrypted STOIC_COACH_DATA_DIR, protect exported files, and avoid recording content the user is not comfortable storing locally.

Risk: Users may treat philosophical coaching as a substitute for mental health care during crisis situations.

Mitigation: Use the skill as philosophy practice only, pause exercises when crisis signs appear, and seek professional or emergency support when needed.

## Reference(s):

- [README](README.md)
- [Coach Guide](references/coach-guide.md)
- [Daily Flows](references/daily-flows.md)
- [Example Session](references/example-session.md)
- [Exercises](references/exercises.md)
- [Quotes](references/quotes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Conversational text and Markdown summaries with inline shell commands; JSON or Markdown files when the user requests export.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local plaintext JSONL journaling under ~/.stoic-coach or STOIC_COACH_DATA_DIR; no external network transfer is described in the security evidence.]

## Skill Version(s):

1.4.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
