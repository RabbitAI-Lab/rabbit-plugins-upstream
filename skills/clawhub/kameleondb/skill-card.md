## Description: <br>
KameleonDB helps agents store, evolve, query, and optimize structured data without designing schemas upfront. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[marcosnataqs](https://clawhub.ai/user/marcosnataqs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to manage persistent structured state for contacts, tasks, knowledge bases, API ingestion, CRM-style systems, and historical queries. It is most relevant when an agent needs to create or evolve schemas, insert or update records, generate SQL, and optimize storage based on usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives agents broad authority over a persistent database, including schema changes, SQL queries, record updates, deletion, imports, and storage optimization. <br>
Mitigation: Use a dedicated test or agent-only database, avoid production credentials, restrict database permissions, and require explicit rules for schema changes, SQL execution, imports, deletions, and personal data storage. <br>
Risk: Persistent storage can retain sensitive, personal, or business-critical data beyond the immediate agent session. <br>
Mitigation: Define what data the agent may store, review generated records and schemas, and apply retention, access-control, and data-governance requirements before deployment. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/marcosnataqs/kameleondb) <br>
- [PyPI Package](https://pypi.org/project/kameleondb/) <br>
- [First Principles](https://github.com/marcosnataqs/kameleondb/blob/main/FIRST-PRINCIPLES.md) <br>
- [Architecture Guide](https://github.com/marcosnataqs/kameleondb/blob/main/docs/ARCHITECTURE.md) <br>
- [Example Workflow](examples/workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON, SQL, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Often includes machine-readable JSON examples for KameleonDB CLI workflows.] <br>

## Skill Version(s): <br>
0.1.5 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
