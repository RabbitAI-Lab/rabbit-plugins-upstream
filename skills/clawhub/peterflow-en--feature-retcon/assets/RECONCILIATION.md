---
schema_version: {{SCHEMA_VERSION}}
round_id: {{ROUND_ID}}
status: executing
authority_root: {{AUTHORITY_ROOT}}
target_stage: {{TARGET_STAGE}}
completion_stage: {{COMPLETION_STAGE}}
created_at: {{CREATED_AT}}
confirmed_at: {{CONFIRMED_AT}}
version_control: {{VERSION_CONTROL}}
baseline_ref: {{BASELINE_REF}}
---

# Reconciliation contract

Private local recovery data. Keep mode 0600 and exclude from Git.

## Authority

Record the authoritative location, reason and source of confirmation.

## Confirmed change

Record the superseded behavior, new required behavior, preserved behavior, exclusions, compatibility and migration impact.

## Scope and boundaries

Record this execution's target stage, full completion stage, writable and read-only roots, confirmed deletions and authorized hooks.

## Artifact dependencies and impact

List the affected responsibilities, paths, consumers and counts.

## Conflicts and risks

Record overlapping edits, unavailable baselines, sensitive payloads and unverifiable results.

## Stage checks

- [ ] Requirements
- [ ] Design
- [ ] Tasks
- [ ] Implementation
- [ ] Validation

## Residual signatures

List old terms and behaviors and their disposition.

## Verification baseline

Record the original commands, environment and observations.

## Write-ahead journal

<!-- feature-retcon:journal:begin -->
```json
{{JOURNAL_JSON}}
```
<!-- feature-retcon:journal:end -->

## Execution and blockers

Record each stage's checks, scope changes and blockers. At a pause record the synchronization point, stale downstream work and needed authorization.

## Closure

- [ ] Authoritative artifacts absorb the confirmed assertion.
- [ ] All stages through the endpoint pass, with zero remaining work.
- [ ] Current requirements trace through to completion.
- [ ] All residual hits have a disposition.
- [ ] Status and stale-stage markers reflect reality.
- [ ] The contract is untracked and unstaged.
- [ ] Mechanical verification passes.
- [ ] No live requirement exists only in the contract.

Give evidence for each applicable check. Closure requires independent evidence in addition to this human review.
