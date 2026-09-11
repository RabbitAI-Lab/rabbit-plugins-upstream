## Description:

Conjecture Prover helps agents break down conjectures across domains, explore reductions or proof routes, run validation checks, and produce clearly labeled proof or open-problem reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and external users can use this skill to structure conjecture analysis, generate proof attempts or precise reductions, and package results as reports, proof outlines, validation notes, and reproducible checks. Outputs should be treated as exploratory unless independently verified by qualified domain experts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may generate mathematical proof drafts or reductions that sound conclusive while still depending on unproven analytic steps or numerical evidence.

Mitigation: Require independent expert review before treating any conjecture result as proven, and preserve explicit status labels for proven, numerically verified, conditional, and open claims.

Risk: The bundled Riemann Hypothesis materials include numerical checks that can support exploration but do not establish a proof.

Mitigation: Use the verification script as a reproducibility aid only, and do not present numerical agreement as a substitute for a complete analytic proof.

Risk: Broad trigger terms such as conjecture, proof, and reduction may activate the skill in conversations where a narrower domain workflow is expected.

Mitigation: Confirm the user's intended conjecture domain and desired rigor level before applying the full proof-generation workflow.

## Reference(s):

- [Conjecture Prover skill page](https://clawhub.ai/wangjiaocheng/skills/conjecture-prover)
- [Publisher profile](https://clawhub.ai/user/wangjiaocheng)
- [Conjecture Prover catalog](references/conjecture-prover-catalog.md)
- [Conjecture Prover requirements](references/conjecture-prover-requirements.md)
- [Exemplars](references/exemplars.md)
- [Riemann Hypothesis delivery overview](assets/RH_README.md)
- [Riemann Hypothesis proof route paper](assets/RH_PAPER.md)
- [Riemann Hypothesis verification script](scripts/rh_proof_verify.py)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown reports with optional code snippets, shell commands, validation notes, and status labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May distinguish proven, numerically verified, pending, conditional, and open-problem claims.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
