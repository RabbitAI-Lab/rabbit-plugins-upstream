## Description:

Manage exam anxiety with adaptive breathing exercises, evidence-based study planning, stress visualization, and motivational coaching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External students, parents, adult learners, teachers, and tutors use this skill to assess exam stress, run guided breathing exercises, generate spaced study plans, track stress trends, and receive zone-specific coaching. It is not a substitute for professional mental health care for clinical anxiety or persistent high stress.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stress scores and notes entered by the user are stored locally in plaintext.

Mitigation: Avoid highly sensitive notes on shared or synced devices, and delete stress_log.json when the retained history is no longer needed.

Risk: Breathing and coaching guidance may be mistaken for clinical mental health care.

Mitigation: Use the skill for exam preparation support only; seek professional support for clinical anxiety or persistent high stress.

## Reference(s):

- [Breathing and Relaxation Techniques](references/techniques.md)
- [Evidence-Based Study Planning](references/study-planning.md)
- [Source Repository](https://github.com/voronindenis5/exam-stress-coach)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/exam-stress-coach)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local study_plan.json, stress_log.json, and stress_trend.png files when the user runs the corresponding commands.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
