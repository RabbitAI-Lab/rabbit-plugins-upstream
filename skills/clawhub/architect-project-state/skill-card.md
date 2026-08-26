## Description:

Architect Project State helps agents maintain a versioned, source-traceable architectural project brief, decision state, change log, open-question register, and bounded task pool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caninlew](https://clawhub.ai/user/caninlew)

### License/Terms of Use:

MIT-0

## Use Case:

Architects, design teams, and agents use this skill to turn design briefs, client meeting notes, consultant feedback, planning conditions, and later revisions into auditable project-state files. It is intended for controlled handoff and state maintenance, not for generating design ideas or imitating an architect's style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates project-state and change-log files inside a chosen project root.

Mitigation: Confirm the intended project root before use, keep writes inside that root, and review the paths touched after each run.

Risk: Architectural records may be mistaken for client commitments, statutory conclusions, or professional judgments.

Mitigation: Require human review and explicit approval for client commitments, statutory conclusions, professional interpretations, and external issue actions.

Risk: Unconfirmed or lower-authority source material could be promoted into current project state if reviewed carelessly.

Mitigation: Preserve source authority, confirmation status, attribution, conflicts, and open questions; do not treat unconfirmed notes as confirmed decisions.

## Reference(s):

- [Project-state schema](references/state-schema.md)
- [Server-resolved GitHub source](https://github.com/caninlew/evidence-driven-project-state/tree/main/skills/architect-project-state)
- [ClawHub skill page](https://clawhub.ai/caninlew/skills/architect-project-state)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown project-state records, change logs, registers, and task tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an explicitly confirmed project root and preserves prior state versions instead of overwriting them.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
