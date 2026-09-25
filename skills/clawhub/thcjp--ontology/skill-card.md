## Description:

A typed knowledge graph engine that helps agents represent memory as validated entity-relationship records with schema constraints, append-only JSONL history, traversal queries, and cross-skill contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to maintain local structured memory as a typed knowledge graph, validate graph changes before commit, query relationships, and coordinate graph-backed work across skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes durable local graph memory and can guide exec-based operations.

Mitigation: Install only for deliberate graph-memory tasks, review proposed commands before execution, and keep the writable graph location scoped to the intended project.

Risk: The artifact describes credential references and callback URLs, which could expose sensitive data or send data to untrusted endpoints if misused.

Mitigation: Keep raw secrets out of the graph, store only secret references, and avoid untrusted callback URLs.

Risk: Rollback behavior is described but should not be assumed without implementation verification.

Mitigation: Verify rollback behavior with non-sensitive test data before relying on it for important graph changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ontology)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with JSON, YAML, JSONL, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces proposed graph operations, schema guidance, validation steps, and query commands for an agent to execute or review.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
