## Description:

Explain difficult concepts, practice related questions, record mistakes and sources, and schedule the next review from actual results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hznetnewpower](https://clawhub.ai/user/hznetnewpower)

### License/Terms of Use:

MIT-0

## Use Case:

Learners use this skill to work through difficult concepts with progressive hints and practice, then keep track of mistakes, reference answers, and review dates. It supports ongoing review based on actual responses rather than generating flashcards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Study questions, answers, and feedback are saved as plaintext in the agent workspace and may contain private learning material.

Mitigation: Protect the active agent workspace and avoid storing sensitive material unless its local storage is appropriate.

Risk: A review due date does not send an active reminder.

Mitigation: Use a separately requested scheduling workflow when proactive reminders are needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/hznetnewpower/skills/mochi-study-coach)
- [MochiLab homepage](https://mochilab.bz)
- [Structured input contract](references/input.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, JSON]

**Output Format:** [Natural-language explanations and practice prompts, with structured JSON study records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review records include question, answer, source, learner response, feedback, and a calculated due date; due views hide answers.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
