## Description:

Run an engineering simulation and read its result with the Arxyne CLI. Use when the user asks to run a CFD, structural, crash, thermal, acoustic or electromagnetic case, asks which solvers or products are available, or wants the numbers and provenance of a previous run.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arxyne](https://clawhub.ai/user/arxyne)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to select an available solver and product, run a requested engineering simulation, and read back recorded KPIs, gate results, and run provenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A simulation may be run with a product or solver that does not match the requested case, or its result may be overstated.

Mitigation: Choose a product and solver that declare compatibility, and report recorded KPIs and gate verdicts as returned, including any missed target.

## Reference(s):

- [Arxyne skill on ClawHub](https://clawhub.ai/arxyne/skills/arxyne)
- [Arxyne publisher profile](https://clawhub.ai/user/arxyne)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with simulation KPIs, gate verdicts, and recorded run provenance when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports recorded result values as returned]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
