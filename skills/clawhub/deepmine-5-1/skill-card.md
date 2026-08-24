## Description:

A Socratic deep-questioning skill that helps users clarify thoughts, review experiences, shape plans, and organize requirements through SOLO-level diagnosis and structured follow-up questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yueran-wang-warwick](https://clawhub.ai/user/yueran-wang-warwick)

### License/Terms of Use:

CC BY-SA 4.0

## Use Case:

External users and developers use this skill when a user wants help thinking through a decision, retrospective, plan, or requirements conversation without the agent inventing conclusions. The skill guides the conversation with structured questions, records per-turn state, and closes with a user-grounded structured summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional finance, tax, legal, and compliance triage could be mistaken for professional advice.

Mitigation: Treat those outputs as preliminary triage and route consequential legal, tax, or financial decisions to qualified professionals.

Risk: The skill stores user-provided planning details in a per-turn state block.

Mitigation: Avoid entering highly sensitive legal, financial, or business information unless the host platform handles hidden state and logs appropriately.

Risk: The workflow is primarily Chinese-language guided questioning.

Mitigation: Review suitability for the intended users before installing or deploying it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yueran-wang-warwick/skills/deepmine-5-1)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Conversational Markdown, JSON routing outputs, and structured requirement summaries with state blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a per-turn <state> block; closing output uses ===REQUIREMENTS_START=== and ===REQUIREMENTS_END=== markers.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; skill docs identify DeepMine V5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
