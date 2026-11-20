# Phase roles

Include the phase and task IDs, workspace, task list and source decisions, acceptance, minimum read set, direct inputs, rules, relevant previous work, permitted writes and verification environment. For review include the entry snapshot and frozen phase changes. Without a baseline, describe the current-state review and its attribution limits. Hand the assignee only their role. The coordinator owns progress, subsequent assignments and Git operations.

## Implementer

Make the bounded change using current code and predecessor outputs. Keep prior work. Run relevant build or regression commands and report actual changed paths, results and remaining work. A repair packet includes the accepted finding and its basis. Before adding a dependency, abstraction or configuration, identify the unmet requirement. Use boundary parsing and local changes where sufficient. Check the diff for unrelated churn. Return the first failed call and minimum necessary extension if the fix leaves the write scope.

## Reviewer

Read the frozen changes, requirements, relevant callers and standards. Report a conclusion for each dimension:

- **Standards.** Give the location, rule and observed violation. Identify missing project standards explicitly.
- **Requirements.** Look for observable conflicts or omissions within this phase. Check what would break if a suspected unnecessary change were removed. An intentional migration guide or required second implementation has a real consumer.

For each finding include the trigger, location, impact, evidence and suggested correction. Separate actual defects from untested risks and future phases. A clean review identifies its scope. Read-only review leaves production code and task status to their owners.

## Tester

Use the requested user entry point and expected result. Reuse existing tests. Add a nearby test when the old defect could pass the current suite. Report version or digests, working directory, environment, input, command, exit status and observation. Correct a faulty test only while preserving the contract. Reproduce production faults and return them for repair. Mark unavailable environments and unexecuted checks accurately.

## Review receipts

From the workspace root run `python3 <skill-dir>/scripts/check_review.py inputs src/export.py tests/test_export.py`, substituting the reviewed files. Capture the digests at review time and compare them again when review returns. Preserve entry snapshots and original role receipts. Include relevant contracts and configuration, and separate frozen acceptance text from progress that will be updated.

```json
{"phase":"P002","reviewer":"review-session-id","standards":"rules checked and conclusion","requirements":"entry point and conclusion","inputs":{"src/export.py":"digest-at-review"},"findings":[]}
```

For each issue record `issue`, `decision` and `reason`. A dismissed finding uses `"decision":"dismissed"` with a specific reason. Preserve pending and accepted findings in their original receipt. After a fix, request a fresh review and retain the earlier evidence.

On resumption run `python3 <skill-dir>/scripts/check_review.py check receipt.json --phase P002` in the same workspace root. Resolve mismatches before reuse. A passing comparison covers the recorded inputs and adjudication only. The coordinator separately checks independent identities, omitted files and actual test evidence before updating the phase.
