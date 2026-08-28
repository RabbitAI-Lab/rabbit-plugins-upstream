## Description:

Industry Deep-Dive Pipeline turns a topic brief, research materials, vendor case, policy event, or industry question into an approved Markdown deep-dive article with verification, originality review, planning gates, review records, and final evidence packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editors, analysts, and content teams use this skill to convert technology, AI, data, cloud, or enterprise-software source material into a single evidence-backed long-form Markdown article. It is intended for workflows that need source traceability, originality review, human planning gates, deterministic red-line checks, panel review, and a final evidence package before any separate publishing step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read article materials and an optional writing profile supplied for the case.

Mitigation: Keep confidential inputs scoped to the intended case directory, use private writing profiles only by reference, and review the final evidence package before handing it to downstream publishing workflows.

Risk: High-risk facts, dates, policy status, product status, or claims of originality could become misleading if verification gates are bypassed.

Mitigation: Use the fact table, source-tier rules, Gate A approval, final re-check, and bundle validation before treating the article as approved.

Risk: Deterministic scans can flag credentials, private paths, unregistered numbers, and style red lines, but they do not replace human editorial judgment.

Mitigation: Run the machine gate and final bundle validation, then complete the required human read-through for logic, posture, timeliness, and unresolved tensions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/industry-deep-dive-pipeline-skill)
- [Planning Schema](artifact/references/planning-schema.md)
- [Evidence and Originality](artifact/references/evidence-and-originality.md)
- [Writing Profile Interface](artifact/references/writing-profile-interface.md)
- [Replay Evaluation](artifact/references/replay-evaluation.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown case bundle with a JSON machine-gate report and shell validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stops at an approved article draft and evidence package; it does not create publication layouts, social copy, CMS drafts, or publishing actions.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
