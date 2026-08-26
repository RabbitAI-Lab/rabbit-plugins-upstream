## Description:

Personal Health Manager helps users analyze diet, fitness, sleep, weight, health indicators, exam results, medication reminders, and chronic-condition routines while stating that its guidance does not replace professional medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and health-conscious users use this skill for non-diagnostic wellness planning, including meal review, exercise planning, sleep improvement, weight tracking, exam-result explanation, medication reminder templates, and chronic-condition lifestyle routines. It is intended to organize and explain health information, not to provide medical diagnosis or prescription guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may keep local plaintext records of usage patterns, notes, errors, and preferences.

Mitigation: Make memory opt-in, scoped, reviewable, and deletable before using it with sensitive health information.

Risk: The skill includes broad self-improvement instructions that may lead an agent to update the skill's own instructions over time.

Mitigation: Require human review before any changes are written back to the skill instructions or bundled memory file.

Risk: Health guidance could be mistaken for medical advice.

Mitigation: Keep medical disclaimers visible, avoid diagnosis or prescription recommendations, and direct users to professional care for urgent symptoms or clinical decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tables, lists, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May record local usage patterns and preferences when the bundled learner module is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
