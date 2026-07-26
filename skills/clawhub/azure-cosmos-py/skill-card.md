## Description: <br>
Azure Cosmos DB SDK for Python guidance for document CRUD, queries, containers, partitioning, and globally distributed NoSQL data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to draft Python Azure Cosmos DB client code, configure containers and partition keys, and reason about query patterns for NoSQL workloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated examples or CLI commands can create, modify, upsert, delete, or query persistent Azure Cosmos DB resources and may affect billing. <br>
Mitigation: Use least-privilege Cosmos DB credentials, prefer test databases first, and review create, replace, upsert, delete, throughput, and indexing changes before running them. <br>
Risk: Inefficient partition keys or cross-partition queries can increase RU consumption or create hot partitions. <br>
Mitigation: Validate partition key choices and query patterns against the workload, monitor RU usage, and avoid cross-partition queries unless they are necessary. <br>


## Reference(s): <br>
- [Partition Key Strategies](references/partitioning.md) <br>
- [Query Patterns Reference](references/query-patterns.md) <br>
- [Cosmos DB Container Setup CLI Tool](scripts/setup_cosmos_container.py) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with Python and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure Cosmos DB operations that affect persistent cloud resources and billing.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
