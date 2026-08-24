## Description:

DeepMine 5.2 is a Chinese-language Socratic guided-questioning skill that helps users clarify ideas, review experience, articulate value, or shape plans into structured knowledge assets using their own words.

This skill is ready for commercial/non-commercial use.

## Publisher:

[boromi-tech](https://clawhub.ai/user/boromi-tech)

### License/Terms of Use:

CC BY-SA 4.0

## Use Case:

Employees, external users, and developers can use this skill to run a guided reflection workflow for experience extraction, value articulation, and plan or requirements shaping. It is best activated by explicit requests to clarify thinking, review a project, describe value, organize requirements, or prepare a structured plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can activate broadly in a general-purpose agent and may steer ordinary reflection into a multi-turn guided questioning workflow.

Mitigation: Enable it only for explicit requests to clarify thinking, review experience, organize requirements, or produce one of the documented structured outputs.

Risk: The skill includes tax, finance, legal compliance, criminal-risk, budget, internal-system, and business-operations risk labeling.

Mitigation: Treat these labels as prompts for professional review, not as legal, tax, financial, or compliance advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/boromi-tech/skills/deepmine-v5-1-1-0-0)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [LICENSE.md](artifact/LICENSE.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Conversational text with Markdown documents, state blocks, and optional JSON risk summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language workflow; final structured documents are constrained to user-provided wording or explicit unknowns.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact docs identify DeepMine V5.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
