## Description:

Code Mentor helps agents provide interactive programming instruction, code review, debugging guidance, algorithm practice, project coaching, and design-pattern explanations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, learners, and technical teams use this skill to receive structured programming mentoring, debugging help, code review, algorithm practice, and beginner-friendly Python or JavaScript guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad coding-related activation wording may cause the skill to activate in more conversations than intended.

Mitigation: Review activation behavior during deployment and narrow trigger use if the environment needs stricter routing.

Risk: The bundled learning_log.md contains a prior learner profile and stale progress notes that could influence future mentoring responses.

Mitigation: Review, remove, or replace the learning log before installation if prior learner context is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/code-mentor)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Learning Log](references/user-progress/learning_log.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with explanations, code snippets, review comments, and step-by-step practice guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May tailor replies to the user's detected language among the skill's supported languages.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
