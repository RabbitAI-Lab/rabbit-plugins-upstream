# Multi-agent operating rules

1. The orchestrator owns decomposition, conflict resolution, and final delivery.
2. Every task has one owner, one outcome, and an objective acceptance test.
3. Delegate only independent work; do not create agents for trivial sequential
   steps.
4. Maximum active agents: `<number>`.
5. Maximum delegation depth: `<number>`; use `1` unless deeper delegation is
   explicitly justified.
6. Per-task limits: `<time>`, `<tokens>`, `<spend>`, and `<retries>`.
7. Agents may access only listed files, tools, channels, and external systems.
8. External messages, payments, publishing, and destructive actions require the
   authorization stated in the task contract.
9. Agents report evidence, changed artifacts, tests, and unresolved risks.
10. Agents stop when acceptance tests pass, a limit is reached, or the same
    blocker repeats. They do not loop indefinitely.
11. One writer owns a file at a time. Conflicting edits return to the
    orchestrator for integration.
12. Secrets stay in approved secret storage and never enter prompts or reports.
13. The reviewer is independent from the author when risk justifies review.
14. The orchestrator closes temporary agents and bindings after final delivery.
