## Description:

Compares two registered Multisim experiments across circuit topology, settings, measurements, verification results, and artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yxy050208](https://clawhub.ai/user/yxy050208)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to compare a baseline Multisim experiment with a candidate run and explain changed simulation results. It helps distinguish design changes, solver or sampling changes, verification differences, and missing evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads experiment summaries and selected text artifacts to compare runs.

Mitigation: Limit access to the minimum text pages needed to explain differences, and avoid binary artifact export unless the user explicitly requests it.

Risk: Experiment results can be misleading when analysis conditions differ.

Mitigation: Mark incompatible conditions as not directly comparable and state what retest would be needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yxy050208/skills/multisim-compare-experiments)
- [Publisher profile](https://clawhub.ai/user/yxy050208)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown comparison table with concise explanatory notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses two registered experiment IDs and reports evidence-backed differences without exporting binary artifacts unless explicitly requested.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
