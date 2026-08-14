## Description:

Diagnose hardware performance shortfalls by defining measurable problems, applying first-principles models and 5M1E review, and producing evidence-ranked causal trees for root-cause analysis and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, hardware engineers, and multidisciplinary review teams use this skill to turn hardware performance shortfalls into measurable problem statements, causal models, prioritized hypotheses, validation experiments, and engineering questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Diagnostic conclusions may be mistaken for certification, safety sign-off, or proof of causation.

Mitigation: Treat outputs as hypotheses and require qualified engineering review, applicable procedures, and validation tests for safety-critical, regulated, or final root-cause decisions.

Risk: The skill may process supplied engineering and manufacturing details during analysis.

Mitigation: Provide only information appropriate for the agent environment and handle proprietary design, supplier, manufacturing, and test data under the user's internal confidentiality controls.

Risk: The PNG exporter reads user-selected causal-tree JSON inputs.

Mitigation: Run the exporter only on trusted UTF-8 causal-tree JSON files and review generated diagrams for correctness and legibility before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/diagnose-hardware-root-causes-rd)
- [Skill source](artifact/SKILL.md)
- [Causal tree PNG exporter](artifact/scripts/ceae_tree_export.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with optional Mermaid diagrams, causal-tree JSON, shell commands, and PNG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PNG export is local and intended for trusted causal-tree JSON inputs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
