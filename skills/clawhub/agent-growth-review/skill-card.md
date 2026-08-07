## Description:

智能体成长复盘 helps users review a period of learning, work, and human-agent collaboration, then produce an AI-enabled growth report that separates confirmed facts, user feelings, report conclusions, and unconfirmed inferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeasonhaitao](https://clawhub.ai/user/jeasonhaitao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to create a staged growth review for a selected time range, combining available memory, profile, agent, skill, conversation, task, and knowledge materials with a small number of clarifying questions. The skill is intended for personal or team reflection on what changed for the user, what changed for the agent, and what collaboration patterns have become stable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may review broad personal history before the user has clearly approved the scope.

Mitigation: Before running it, define the time range, approved sources, and report save location; withhold approval for Memory write-back until after reviewing the final report.

Risk: A growth report may blend confirmed facts, user feelings, report conclusions, and unconfirmed inferences.

Mitigation: Require uncertain content to be labeled and ask the user to confirm facts and inferences before saving or reusing the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeasonhaitao/skills/agent-growth-review)
- [Conflict analysis reference](artifact/references/conflict-analysis.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown growth report, with an optional same-source Word document when the environment supports it]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language letter-style report; typically includes a human-agent collaboration comparison table, review prompts, and Memory write-back guidance that requires user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
