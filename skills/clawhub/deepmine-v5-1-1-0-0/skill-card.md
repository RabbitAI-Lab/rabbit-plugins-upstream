## Description:

DeepMine V5.1 guides Chinese-language Socratic questioning sessions for idea clarification, experience review, plan shaping, and requirements analysis, ending with a structured summary based on the user's own statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[boromi-tech](https://clawhub.ai/user/boromi-tech)

### License/Terms of Use:

CC BY-SA 4.0

## Use Case:

Chinese-speaking users and agents use this skill to clarify ambiguous thoughts, review experiences, generate plans, and organize requirements through structured follow-up questions. It is intended for reflective thinking support rather than direct expert decision-making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The built-in tax and compliance extractor may be mistaken for legal or tax advice.

Mitigation: Treat extractor output as a lightweight risk prompt and require qualified professional review before acting on tax, legal, or compliance decisions.

Risk: Broad trigger phrases can activate the full questioning workflow during general uncertainty or ordinary planning conversations.

Mitigation: Require explicit user confirmation before activation in deployments where broad Socratic questioning could interrupt normal chat.

Risk: The workflow maintains per-turn state derived from user statements.

Mitigation: Handle conversation state according to the deployment's privacy and retention requirements, especially when users discuss sensitive business or compliance details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/boromi-tech/skills/deepmine-v5-1-1-0-0)
- [Publisher Profile](https://clawhub.ai/user/boromi-tech)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Orchestrator](artifact/orchestrator.md)
- [Risk Extractor](artifact/extractor.md)
- [SOLO Levels](artifact/shared/solo_levels.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language conversational replies, internal routing JSON, and a structured Markdown-style conclusion summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Maintains a per-turn state block and requires final summaries to use only user-provided wording or faithful summaries.]

## Skill Version(s):

1.0.0 (source: server release metadata; skill source states DeepMine V5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
