---
name: jahids-recovery-manager
description: Plan safe recovery from failed or partial agent tasks using checkpoints, idempotency, rollback, and evidence preservation.
---

# JAHIDS Recovery Manager

## Use when
A mission fails, times out, partially completes, or produces an uncertain external state.

## Procedure
1. Stop new side effects and capture current state.
2. Identify the last verified checkpoint and incomplete operations.
3. Determine which operations are idempotent and which may have succeeded externally.
4. Reconcile external state before retrying.
5. Prefer compensating actions or last-known-good rollback where supported.
6. Preserve logs, artifacts, and audit evidence.
7. Resume only within the original authorization and remaining budget.

## Output
A recovery plan with checkpoint, state reconciliation, rollback or compensation, and verification steps.

## Authority boundary
Recovery cannot expand scope or reuse expired approval.
