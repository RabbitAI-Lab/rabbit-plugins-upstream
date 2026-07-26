# Examples

## Small Standalone Repair

Goal: Fix one reproducible export defect.

- Size: Small
- Governance: Lite
- Stage: baseline/reproduction, repair, regression, functional export check
- Files: Active Packet and Loop Runs
- Completion: self-accept only after automatic and exported-artifact evidence pass

Do not create a Program or Milestone.

## Medium Governed Feature

Goal: Add one user workflow spanning API and UI.

- Size: Medium
- Governance: Standard
- Stages 1-3: baseline and vertical slice
- Stage 3: alignment check
- Stages 4-6: integration and primary user flow
- Stage 6: alignment check
- Final: `Ready for Review`; independent QA decides acceptance

Do not mark accepted from Developer evidence alone.

## Long Run Starts Drifting

At stage 6, tests pass but the delivered workflow no longer solves the Owner's original problem.

- Set alignment recommendation to `Locally Compliant, Globally Misaligned`.
- Stop feature expansion.
- Preserve local evidence.
- Ask governance to compare the original outcome, current behavior, and new assumptions.
- Continue only after alignment or rebaseline.

## Repeated Failure

Two loops fail the same core check without narrowing the cause.

- Stop broad edits.
- Record failed commands and evidence.
- Set `Needs Fix` when a bounded diagnostic action exists.
- Set `Blocked` when environment or authority is missing.
- Do not reset as a new Milestone.
