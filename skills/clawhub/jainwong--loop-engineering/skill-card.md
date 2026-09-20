## Description:

Loop Engineering helps agents manage complex multi-step work through explicit planning, execution, observation, evaluation, repair, and stopping loops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jainwong](https://clawhub.ai/user/jainwong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent users use this skill to structure complex work such as code generation, debugging, design implementation, content creation, tool chaining, and data analysis when the task needs iterative verification and correction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent cross-task workflow memory and detailed trace logging may retain sensitive task information.

Mitigation: Use per-project isolation, redaction, review, and deletion controls before enabling this skill on sensitive work.

Risk: Using the skill in shared workspaces may expose credentials, private customer data, proprietary code, or regulated information through retained traces.

Mitigation: Avoid shared workspaces and sensitive tasks unless clear data-handling controls are in place.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jainwong/skills/loop-engineering)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with YAML and code block examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include loop state cards, observation and evaluation records, repair steps, trace summaries, and experience-bank entries.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
