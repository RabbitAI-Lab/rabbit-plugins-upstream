## Description: <br>
Ontology helps an agent create, validate, relate, query, and maintain a typed local knowledge graph for structured memory, task dependencies, project state, and cross-skill contracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill when they want an agent to maintain structured project memory as typed entities and relationships, including tasks, goals, events, documents, credentials by reference, and dependency graphs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent graph memory may retain sensitive or outdated information in local ontology files. <br>
Mitigation: Review memory/ontology contents before sharing or deployment, and avoid recording sensitive values. <br>
Risk: Credential entities could expose secrets if direct passwords, tokens, or keys are written into the graph. <br>
Mitigation: Store only secret references such as secret_ref values and keep actual credentials in an external secret manager. <br>
Risk: Append-only graph logs preserve historical records even after later updates or deletions. <br>
Mitigation: Sanitize or rotate graph history when data retention requirements change. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/thcjp/skills/ontology) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with command examples and JSON, JSONL, and YAML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide the agent to create or update local ontology files such as schema.yaml and graph.jsonl.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
