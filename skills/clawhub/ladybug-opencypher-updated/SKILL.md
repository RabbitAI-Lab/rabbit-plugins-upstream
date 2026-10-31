---
name: ladybug-opencypher-updated
description: "Designs and queries LadybugDB graphs with openCypher. Use for schemas, imports, query debugging, transactions, full-text search and Neo4j query adaptation, with local Python helpers."
license: MIT-0
metadata:
  openclaw:
    emoji: "🐞"
    requires:
      anyBins: [python3, python]
---

# LadybugDB openCypher

## Runtime and ownership

Identify the database, owning process and authorized reads/writes/schema changes. Use the owning application's API for a live read-write database: multiple connections in one process are supported; multiple processes cannot share read-write access.

Documentation-only tasks need no runtime. For execution, use the project's Python environment and run `<python> <skill-dir>/scripts/check_env.py --smoke` (in-memory only). The binding is `ladybug`, pinned in [requirements.txt](requirements.txt); installing this skill does not install it. [API reference](references/api-reference.md) covers environment setup, native-load failures and requested OpenClaw installation checks.

## Query and verify

Inspect the schema first: node primary keys, relationship direction, properties and multiplicity. Preserve parallel relationships/evidence IDs even when endpoints match. Use the [API reference](references/api-reference.md) for imports, parameters, async and FTS; [workflow patterns](references/workflow-patterns.md) for Neo4j differences and unexpected results.

The helper defaults to engine-enforced read-only access:

```text
<python> <skill-dir>/scripts/run_cypher.py /path/to/graph.lbdb --command "MATCH (n:Paper) RETURN n.id LIMIT 10" --print-rows
```

- Bind values with `--params`/`--params-file`; validate identifiers separately. Use `--file` for reviewed multiline Cypher.
- Authorized mutations need `--write`; creation needs `--write --create`, which refuses existing paths. Do not escalate after a read-only error.
- Atomic batches need `BEGIN TRANSACTION; ...; COMMIT;`. Otherwise statements commit separately; inspect partial state before retrying. Follow the application's backup/migration procedure.
- Defaults: 30-second timeout, 256 MiB buffer, 20 preview rows per statement (`--timeout-ms`, `--buffer-mib`, `--max-rows`). Preview limits do not bound execution/result memory; use selective predicates and bounded traversals, plus query `LIMIT` where appropriate.
- Read-only database access does not restrict host files/network. Review `COPY`, `LOAD`, `CALL`, extensions and paths; use trusted absolute import paths. Helpers make no HTTP calls or automatic installations, but queries/extensions can access resources.
- Read back writes and check properties, direction and identity, not just counts. Close results/connections/databases on failure too; the helper handles this.

Test engine upgrades and recovery on copies, never the only database. [Helper tests](scripts/test_helpers.py) use temporary databases. Report actual checks and unresolved limits.

Community-maintained under MIT-0; based on [trenza1ore/ladybug-opencypher](https://clawhub.ai/trenza1ore/skills/ladybug-opencypher).
