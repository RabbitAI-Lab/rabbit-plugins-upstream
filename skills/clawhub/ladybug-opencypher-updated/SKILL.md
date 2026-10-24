---
name: ladybug-opencypher-updated
description: "Design and query LadybugDB graphs with openCypher. Use for schemas, data imports, query debugging, transactions, full-text search and Neo4j query adaptation, with local Python helpers."
license: MIT-0
metadata:
  openclaw:
    emoji: "🐞"
    requires:
      anyBins: [python3, python]
---

# LadybugDB openCypher

Work with LadybugDB property graphs using openCypher and Python. This skill guides schema design, data loading, query authoring and result verification, with local helpers for checking the runtime and executing queries.

## What it covers

- **Graph modelling:** define typed node and relationship tables, primary keys, direction, properties and multiplicity.
- **Data workflows:** import CSV, Parquet or dataframe data; use parameterized queries and explicit transactions; verify persistent results and parallel relationships.
- **Query development:** write bounded traversals and shortest-path queries, debug counts and scope, and adapt Neo4j queries to LadybugDB semantics.
- **Full-text search:** define and query indexes using the LadybugDB FTS extension, with guidance on prerequisites and procedure arguments.
- **Python execution:** check the selected environment and run Cypher with read-only defaults, explicit write/create options, timeouts and bounded result previews.

Use it when building a local graph, exploring an existing database, troubleshooting a query or integrating LadybugDB into an application. Database access follows the application's ownership model; full-text search requires the corresponding engine extension.

## 1. Select the runtime and database owner

Identify the target database, its owning process, and whether the task permits reads, writes, schema changes, or creation. If an application owns a read-write database, use its existing API rather than opening that file from a second process. Multiple concurrent connections within one owning process are supported; multiple processes cannot share a read-write database.

Select the project's Python environment. For a shared local installation, check `~/.local/share/ladybug-opencypher-updated/venv/bin/python` (Windows: use the selected environment's `Scripts/python.exe`). Resolve all relative script paths from this skill's directory, not the current working directory. Run:

```text
<python> <skill-dir>/scripts/check_env.py
```

Use the **`ladybug`** Python package with the dependency pinned in [requirements.txt](requirements.txt). Installing a skill does not install the database bindings. When dependency installation is authorized, use a dedicated environment and that requirements file; do not modify the system Python or start a database service. See the [runtime and API reference](references/api-reference.md) for compatibility details.

**Done when:** the selected interpreter passes the check and the database access route and write scope are explicit. Documentation-only work does not require installed bindings.

## 2. Match the schema and query semantics

Inspect the existing schema before proposing DDL. Ladybug uses schema-first node and relationship tables; every node table has a primary key. Define relation direction, properties and multiplicity explicitly. Do not assume labels, procedures or Neo4j syntax are interchangeable.

For new tables, imports, async Python, parameters and FTS signatures, consult [API reference](references/api-reference.md). For wrong counts, paths, unsupported clauses and migration differences, use [workflow patterns](references/workflow-patterns.md). Bound traversals and anchor queries with selective predicates. Preserve distinct relationships between the same endpoints; do not merge evidence solely because node pairs match.

**Done when:** the proposed query names real schema elements and its path, multiplicity and identity semantics match the requested result.

## 3. Execute the scoped operation

Read an existing local database with the helper's default engine-enforced read-only mode:

```text
<python> <skill-dir>/scripts/run_cypher.py /path/to/graph.lbdb --command "MATCH (n:Paper) RETURN n.id LIMIT 10" --print-rows
```

Use `--params` or `--params-file` for bound values, not string interpolation. A JSON parameter file is preferable for complex values. Use `--file` for reviewed multi-line Cypher. Paths in `COPY` and `LOAD FROM` are resolved by the database process; use explicit trusted absolute paths.

For authorized mutations add `--write`. For an explicitly requested new database use `--write --create`; existing paths are refused. Use explicit `BEGIN TRANSACTION; ...; COMMIT;` when a batch must be atomic. Semicolon-separated statements are not automatically one transaction. Keep migrations/backups under the application's existing procedure; the helper is not a migration or curation service.

The helper sets a 30-second query timeout and a 256 MiB buffer pool, adjustable with `--timeout-ms` and `--buffer-mib`. Output previews default to 20 rows per statement, adjustable with `--max-rows`. A preview cap does **not** cap query execution or engine result memory; use query-side `LIMIT` and bounded traversals too.

Read-only database mode protects database data, not the host filesystem or network. Review `COPY`, `LOAD`, `CALL`, extension loading and file paths before executing even a read query. The helper executes supplied Cypher; it does not sandbox arbitrary queries. The bundled scripts make no HTTP requests, install no dependencies/extensions, and access only the supplied database/query/parameter paths directly. Queries may access additional resources according to the selected engine and extensions.

**Done when:** execution succeeds within the authorized scope, or the exact error is reported without retrying in write mode or changing dependencies automatically.

## 4. Verify the result and availability

Verify expected entities, relation direction, parallel relationships, properties and returned evidence, not only a row count. After writes, read back the affected records. Close query results, connections and database handles; the helper does this on success and failure. Treat format upgrades as migrations and test recovery on copies before opening an older database with a newer engine.

When installing in OpenClaw, verify the installed version and, for every intended agent, `eligible`, `disabled`, `blockedByAgentFilter` and `modelVisible` using `openclaw skills info ladybug-opencypher-updated --agent <id> --json`. Global installation shares files but does not override agent skill filters. Check the selected Python separately with `check_env.py`; discovery alone does not prove script readiness. Keep changes within the approved agent scope and do not restart the Gateway merely to refresh skills.

**Done when:** the outcome is verified, or unverified criteria are stated explicitly. Use [runtime smoke tests](scripts/test_helpers.py) only on the temporary databases they create, never on a user corpus.

## Sources and attribution

Official LadybugDB documentation:

- [Installation](https://docs.ladybugdb.com/installation/)
- [Python API](https://docs.ladybugdb.com/client-apis/python/)
- [Connections and concurrency](https://docs.ladybugdb.com/concurrency/)
- [Neo4j differences](https://docs.ladybugdb.com/cypher/difference/)
- [Transactions](https://docs.ladybugdb.com/cypher/transaction/)
- [Database migration](https://docs.ladybugdb.com/migrate/)

Community-maintained skill under MIT-0, with attribution to [trenza1ore/ladybug-opencypher](https://clawhub.ai/trenza1ore/skills/ladybug-opencypher).
