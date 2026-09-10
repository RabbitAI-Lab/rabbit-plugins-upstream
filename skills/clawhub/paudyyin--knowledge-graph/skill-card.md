## Description: <br>
Builds a local knowledge graph for agent memory, JSONL/RDF conversion, OWL reasoning, SPARQL querying, and natural-language hybrid querying. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to persist entity and relationship memory, validate ontology schema constraints, convert between JSONL and RDF, run semantic reasoning, query with SPARQL or natural-language patterns, and export graph data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create and retain local knowledge-graph memory files that may include personal, contact, message, or account-reference data. <br>
Mitigation: Review graph contents before retention or sharing, store only necessary data, and apply local retention or deletion practices appropriate for the workspace. <br>
Risk: Sensitive secrets could be mishandled if users store raw passwords, tokens, or API keys in graph entities. <br>
Mitigation: Store only secret references, never raw credentials, and keep actual secrets in an approved secret store. <br>
Risk: Dependencies are version-ranged rather than pinned, which can reduce reproducibility across installs. <br>
Mitigation: Use pinned dependencies or a lockfile for production or repeatable deployments. <br>


## Reference(s): <br>
- [Architecture](references/ARCHITECTURE.md) <br>
- [Query Reference](references/queries.md) <br>
- [Ontology Schema Reference](references/schema.md) <br>
- [Domain-Kit ontology namespace](https://domain-kit.midea.com/ontology/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local JSONL graph memory and RDF export files when the agent follows the skill.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
