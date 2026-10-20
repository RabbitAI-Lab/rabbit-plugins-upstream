## Description:

A full-stack knowledge graph skill for agent memory CRUD, planning, cross-skill relationship sharing, OWL semantic reasoning, SPARQL querying, natural-language hybrid queries, and RDF export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paudyyin](https://clawhub.ai/user/paudyyin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to store local entity-relationship memory, validate graph records, convert JSONL data to RDF, run semantic reasoning, query with SPARQL or natural language patterns, and export graphs for ontology tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent graph storage may record personal, project, message, document, account, and credential-reference metadata.

Mitigation: Use the skill only for intended local memory, avoid raw secrets, and store only secret references such as external credential-store identifiers.

Risk: SPARQL, natural-language query, RDF import, and export paths have weak containment and input-safety controls for untrusted use.

Mitigation: Keep these interfaces local or trusted unless escaping, path and URL allowlists, query limits, and dependency pinning are added.

## Reference(s):

- [Architecture - Domain-Kit OWL Integration](references/ARCHITECTURE.md)
- [Query Reference](references/queries.md)
- [Ontology Schema Reference](references/schema.md)
- [Domain-Kit Ontology Namespace](https://domain-kit.midea.com/ontology/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python and shell command examples, JSON/JSONL records, RDF serializations, and query results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or read local JSONL graph storage and may export RDF files when invoked through the provided tooling.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
