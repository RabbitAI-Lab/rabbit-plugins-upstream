## Description:

A prompt-only skill that helps agents clarify ambiguous or incomplete requests, align on user intent, and produce structured, higher-quality answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[edde-101](https://clawhub.ai/user/edde-101)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and employees can use this skill to improve unclear or underspecified prompts by identifying intent, constraints, assumptions, and gaps before producing a structured answer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can shape answer structure for ambiguous requests and may carry Chinese-language phrasing into responses.

Mitigation: Set system or user language and formatting preferences explicitly when deploying it in workflows that require another language or house style.

Risk: Prompt optimization can introduce assumptions when user requirements are incomplete.

Mitigation: Require the agent to surface blocking gaps and assumptions before proceeding on high-impact or externally visible answers.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/Edde-101/SimpleAgent/tree/main/skills/prompt-optimizer)
- [ClawHub skill page](https://clawhub.ai/edde-101/skills/prompt-optimizer-2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured text, tables, checklists, summaries, assumptions, and clarification questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-only output; no code execution, data access, persistence, or hidden privileged behavior.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
