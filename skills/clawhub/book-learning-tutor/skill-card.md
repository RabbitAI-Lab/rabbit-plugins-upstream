## Description:

Course-ifies local book files into structured lessons and guides learners through prep, Feynman explanations, practice gates, spaced review, recitation homework, and progress tracking; optional online acquisition is available only when explicitly authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fangyuan-3149](https://clawhub.ai/user/fangyuan-3149)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn local book files into structured courses and run an agent-led tutoring loop with generated lesson files, quizzes, review cards, homework, and progress updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional online acquisition can run untrusted source rules through local JavaScript and broad network fetching.

Mitigation: Keep online acquisition disabled unless explicitly needed, avoid importing untrusted source subscriptions, and review or disable the JavaScript bridge before use.

Risk: Weak safeguards in the optional fetching path can expose users to unsafe or unintended network behavior.

Mitigation: Use the local book-processing path by default, fetch only confirmed public sources within the user's authorization scope, and change HTTPS verification to on.

Risk: Learner-profile and progress files may retain personal study information.

Mitigation: Periodically review or delete files under storage/ and related progress data according to the user's retention needs.

## Reference(s):

- [Book Learning Tutor on ClawHub](https://clawhub.ai/fangyuan-3149/skills/book-learning-tutor)
- [Source Acquisition](artifact/references/source_acquisition.md)
- [Source Selection and Evaluation](artifact/references/source_selection.md)
- [Teaching Patterns](artifact/references/teaching_patterns.md)
- [Self-Evolution Spec](artifact/references/self_evolution.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown lessons and chat guidance, with JSON progress files and shell commands for local processing.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local course and storage files; optional acquisition can perform network fetching only with explicit authorization.]

## Skill Version(s):

0.1.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
