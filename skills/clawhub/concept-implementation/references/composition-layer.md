# Composition Layer

Implement WYSIWID completion → read-only binding → call semantics. Modular monoliths, query
interfaces, directory layout, and mediators are repository choices, not the paper's only
implementation.

Default to a mediator when rules and calls are few and explicit. Compile fine-grained
synchronizations into orchestration functions without serializing allowed concurrency or consuming
future outputs early. Consider a rule engine when rules evolve independently, match several events,
or require provenance; verify its real `when`/`where`/`then`, flow, deduplication, and persistence
semantics.

Documentation flows group responsibility; runtime flows are causal instances. Record flow/request,
completion identity, rule, inputs, and outputs. Correlate repeated actions by object identity. Match
named success/error fields rather than assuming empty output means success.

DTO and protocol adapters stay at the application edge and call composition entry points. Preserve
authorization on actions and queries. Concepts expose actions and abstract state; composition binds
and calls but never replaces atomic invariants with query-before-write checks. Provenance, outbox,
retry, and idempotency records are orchestration data; independent business state suggests a new
concept.

Zero `where` rows emit no call; many rows emit many binding sets. Define success, refusal, timeout,
and failure for request entries. Background entries may omit responses but still require failure
handling. Retries need durable idempotency; compensation records history and does not promise
restoration.

Use a cross-concept transaction only when all storage participates, external effects are isolated,
and the contract permits it. Publish completion after commit or through an outbox. Transactions do
not replace synchronization error behavior. Check reachable cycles for termination, retry budgets,
or controlled continuation with observable limit failures.

Move staged specifications to their owning modules/packages and update the index. CI verifies no
concept references, public-interface use, OPs, invariants, conjunctive triggers, zero/many queries,
concurrent request isolation, errors, and replay deduplication.
