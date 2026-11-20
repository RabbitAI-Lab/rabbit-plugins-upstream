# Worked cases

| Change | Expected treatment |
| --- | --- |
| A PDF-only export with existing tasks now needs a format selector. Only the requirement is authorized today. | Update requirements, record stale design and tasks, pause the same round. Closure reaches at least the task stage. |
| An implemented asynchronous feature changes. The user wants design first. | `target_stage=design`, `completion_stage=implementation`. Resume with the same round after authorization. |
| A design term changes before any downstream work exists. | Requirements and design checks can close a design-only round with appropriate evidence. |
| A live notification rule changes in one authorized pass. | Follow the affected layers up through implementation and the required tests in the same round. |
| T020 covers both email and inbox notifications, now accepted separately. | Split responsibilities, keep lineage and update active references and phase ownership. |
| Four old migration tasks collapse into two meaningful outcomes. | Preserve valid work and evidence, identify the successor tasks and repair dependencies. |
| An uncommitted spec already includes edits in the affected section. | Use the current bytes as the baseline if ownership and authorization are clear. Preserve unrelated edits. |
| The user stops in a directory without Git. | Pause. For an explicit undo, restore embedded bytes in reverse order, verify baseline and references, close with restored evidence. |
| Docs, code and tests live in different repositories. Tests are read-only. | Carry all three roots in the assessment. A required test edit beyond the authorized roots blocks acceptance. |
| Old field names are gone but a parser still accepts the old shape. | Classify the old behavior and its tests. Only current compatibility requirements can retain it. |
| A user requests undo after closure and later edited one target. | Inspect the archive. Reopen and restore preflight all targets. On drift preserve all targets and explain the conflict. Finish a successful restoration with an independent baseline check and a separate archive. |
