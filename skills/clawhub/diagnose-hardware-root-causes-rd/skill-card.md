## Description:

Diagnose hardware performance shortfalls with measurable problem definition, first-principles models, equation-led decomposition, 5M1E coverage, multidisciplinary review and evidence-ranked causal trees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Engineers and hardware teams use this skill to turn measured performance shortfalls into testable causal models, prioritized root-cause hypotheses, validation experiments, and engineering questions. It is intended for decision support and investigation planning, not standalone safety certification or regulatory sign-off.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated hypotheses or causal trees may be mistaken for proof of causation, safety certification, or regulatory conclusions.

Mitigation: Treat outputs as engineering decision support; require discriminating tests and qualified engineering review for safety-critical or regulated hardware work.

Risk: The local PNG exporter operates on user-selected causal-tree JSON input and output paths.

Mitigation: Run the exporter only on intended local files, then review the image for legibility, clipping, and consistency with the source causal tree.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/diagnose-hardware-root-causes-rd)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with optional JSON causal-tree input and PNG export workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce measurable problem statements, evidence tables, causal trees, prioritized hypotheses, validation experiment plans, engineering questions, and local PNG tree exports.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
