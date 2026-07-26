# Safety And Context

## Hard Stops

Stop before:

- requesting, reading, storing, or exposing secrets;
- account login or session reuse;
- production or non-sanitized customer data;
- paid resources or production changes;
- system-level installation or privileged host configuration;
- destructive deletion, migration, overwrite, reset, force push, or history rewrite;
- protected architecture, security policy, or technology-stack replacement;
- action outside current authority.

Ask for approval with exact scope, impact, rollback, and evidence plan. Record the approval source and expiry without recording secret values.

## Safe Project-Local Actions

Unless project rules prohibit them, the agent may usually:

- inspect repository files;
- edit authorized source and tests;
- install declared project dependencies;
- run project-local builds and tests;
- create local fixtures and disposable test output;
- update authorized project-local state.

Do not confuse project-local dependency installation with system-level installation.

## Context Budget

Default read order:

1. Active Packet.
2. One current action and linked acceptance criteria.
3. Relevant source and tests.
4. Verification config.
5. Last three to five loop records.

Do not read all historical logs or Milestones unless debugging drift or state inconsistency.

Keep:

- Active Packet under roughly 200 lines;
- current context summary under roughly 40 lines;
- one immediate next action;
- command summaries short, with paths to raw logs.

Stop as `Blocked` or `Invalid State` when the required context cannot be made coherent within budget.

## Persistent Data

Never store:

- secrets or environment values;
- private customer data;
- full private documents;
- full chat transcripts;
- hidden reasoning;
- large logs;
- unnecessary machine-specific paths.

Store evidence references and concise observable summaries.
