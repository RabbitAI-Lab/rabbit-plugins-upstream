## Description:

Evaluates whether an agent skill is safe to run and effective for its intended job across safety, quality, benchmarking, and version-comparison reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lienong1122334](https://clawhub.ai/user/lienong1122334)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, maintainers, and reviewers use this skill to evaluate agent skills for safety, effectiveness, regressions, and release readiness. It guides static checks, prompt and assertion design, transcript review, risk findings, and final recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Evaluation conclusions can be mistaken for guarantees, especially when runtime tests are skipped or external APIs are unavailable.

Mitigation: Treat reports as review guidance and confirm skipped runtime behavior, unavailable API results, and high-impact findings before deployment.

Risk: Stale backup files can confuse reviewers about which workflow is authoritative.

Mitigation: Remove or clearly exclude backup material before publication so reviewers rely on the current SKILL.md, scripts, and references.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lienong1122334/skills/linkfox-skill-evaluator)
- [Red Flag Details](artifact/references/red-flag-details.md)
- [Vertical Skill Review Extension](artifact/references/vertical.md)
- [Process-Flow Skill Review Extension](artifact/references/process-flow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report text with optional inline shell commands and JSON-capable pre-check output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include safety verdicts, quality findings, scope and confidence notes, and release recommendations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
