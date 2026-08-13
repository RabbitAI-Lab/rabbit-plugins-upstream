## Description:

Manage exam anxiety with adaptive breathing exercises, evidence-based study planning, stress visualization, and motivational coaching.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External students, parents, tutors, and adult learners use this skill to assess exam stress, receive breathing or coaching prompts, generate spaced study plans, and track stress trends during exam preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stress levels and optional notes can be saved in local JSON files.

Mitigation: Avoid recording highly sensitive details in notes, especially on shared or backed-up machines.

Risk: The study planner can write output to a user-provided path.

Mitigation: Review the `plan --output` destination before running the command.

Risk: The skill provides stress-management support but is not a substitute for clinical care.

Mitigation: Use professional mental health support for clinical anxiety, persistent severe stress, or safety concerns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/exam-stress-coach)
- [Server-Resolved GitHub Provenance](https://github.com/voronindenis5/exam-stress-coach)
- [Breathing & Relaxation Techniques](references/techniques.md)
- [Evidence-Based Study Planning](references/study-planning.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON or PNG files created by the local script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled script can write stress_log.json, study_plan.json or a user-specified plan path, and stress_trend.png when matplotlib is available.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
