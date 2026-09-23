## Description:

主动式代理 guides an AI agent to preserve context, run heartbeat checks, use WAL-style memory updates, and proactively surface next actions under human oversight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to make an AI assistant more proactive for context persistence, recovery after compression, task monitoring, tool migration, and self-improvement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill encourages broad proactive behavior with file, command, API, and memory workflows.

Mitigation: Require explicit approval for shell commands, file writes, external calls, scheduled actions, and persistent memory changes.

Risk: Persistent memory workflows can retain sensitive data longer than intended.

Mitigation: Avoid providing secrets or sensitive personal data unless the agent platform provides clear memory inspection and deletion controls.

Risk: Autonomous or scheduled actions can overreach the user's intended scope.

Mitigation: Use bounded triggers, human review checkpoints, and clear stop conditions for proactive or heartbeat-driven work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/proactive-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured status, summaries, command examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include memory-update guidance, recovery checklists, heartbeat actions, migration steps, and validation results.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 3.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
