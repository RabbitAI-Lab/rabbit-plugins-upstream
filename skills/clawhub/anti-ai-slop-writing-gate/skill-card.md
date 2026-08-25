## Description:

Detect or minimally edit formulaic AI-style prose while preserving the writer's voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mwclaw](https://clawhub.ai/user/mwclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external contributors, and writing-focused agents use this skill to detect formulaic AI-style prose, make minimal edits, or run a silent pre-send writing gate while preserving the writer's voice and factual support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pre-send mode silently polishes substantive replies, which can reduce visibility into wording changes for important communications.

Mitigation: Use detect or edit mode when visible change notes, auditability, or approval before wording changes are needed.

Risk: Style-pattern findings could be misread as proof that a text was written by AI.

Mitigation: Use findings only to evaluate writing patterns; do not assign authorship claims or AI-likelihood scores.

Risk: Minimal edits can still change certainty, sourcing, or the writer's voice if applied too broadly.

Mitigation: Preserve facts, uncertainty, and voice signals, and check edits against the provided pass/fail evals before returning them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mwclaw/skills/anti-ai-slop-writing-gate)
- [Publisher profile](https://clawhub.ai/user/mwclaw)
- [Pattern Guide](references/patterns.md)
- [Pass/Fail Evals](references/evals.md)
- [Quick Checklist](references/checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, analysis, guidance]

**Output Format:** [Plain text or Markdown, depending on mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edit mode returns a clean version with change notes; detect mode returns findings; pre-send mode returns only the corrected reply.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
