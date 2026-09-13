## Description:

Handoff helps agents continue, inspect, or explicitly set up repository task handoffs while checking legacy handoff deployments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[snowsonz](https://clawhub.ai/user/snowsonz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Handoff to maintain task continuity across supported CLIs, inspect handoff state, configure explicit user-level entry points, and migrate verified legacy handoff deployments without copying runtime files into repositories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make persistent handoff workflow, setup, and migration changes.

Mitigation: Install and enable it only when a persistent handoff workflow is desired; review the target CLI rule files before running setup.py enable.

Risk: Legacy migration can remove verified old handoff files and strip a marked AGENTS.md handoff block.

Mitigation: Run migrate.py status first and review reported legacy paths; stop if the migration reports blocked or unexpected ownership.

Risk: The operating instructions are primarily in Chinese, which can create review friction for teams that do not read Chinese.

Mitigation: Have a Chinese-reading reviewer confirm the protocol boundaries before deployment, especially setup, migration, and handoff ownership rules.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/snowsonz/skills/agent-handoff-skill)
- [Runtime Protocol](PROTOCOL.md)
- [Global Runtime Maintenance Reference](references/protocol.md)
- [Discovery and Trigger Compatibility](references/compatibility.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and task-state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write repository task state only when the handoff protocol allows it; setup and migration commands require explicit user intent or documented legacy-cleanup conditions.]

## Skill Version(s):

0.3.0 (source: release metadata, VERSION, references/protocol.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
