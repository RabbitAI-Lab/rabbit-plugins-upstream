## Description:

Multi Agent Collab orchestrates role-based agent collaboration by collecting proposals, applying critic filtering, and selecting or combining the strongest results with a scorer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to coordinate multiple specialist agents on complex tasks that benefit from proposal, critique, and integration stages. It is useful when an auditable collaboration trace and explicit quality gate are needed before choosing a final answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local learner can record operation history, error notes, and preference values in learned_patterns.json.

Mitigation: Do not store secrets or sensitive personal data in learner notes or preferences, and review learned_patterns.json before sharing the skill directory.

Risk: Caller-injected roles, critic logic, and scoring logic can produce or select poor proposals if they are misconfigured.

Mitigation: Review the injected roles, critic, and scorer for the target task, and run the bundled self-test before relying on a new configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qq435912743/skills/multi-agent-collab)
- [ClawHub Publisher Profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSON orchestration results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes proposal records with selected best result, critic notes, scores, and kept proposal counts when run through the bundled script.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
