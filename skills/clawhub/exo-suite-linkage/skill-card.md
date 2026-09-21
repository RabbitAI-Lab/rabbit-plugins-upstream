## Description:

Links hfpclawer, expflow-pde, and omega-architect through file and CLI contracts so research agents can move from literature evidence to experiments and machine-checked Lean proofs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to connect literature discovery, experiment tracking and HPO, and Lean proof workflows through explicit handoff artifacts. It helps agents preserve provenance, cost tiering, and verification status across the toolchain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the referenced third-party CLI tools may introduce dependency, network, and workspace file risks.

Mitigation: Pin exact package or tag versions when reproducibility matters, review packages before installation, and run the workflow in a project workspace where generated files and network access are expected.

Risk: A workflow output may overstate proof status when the proof layer did not run or did not compile successfully.

Mitigation: Label missing or failed proof steps as unverified and treat only compiler-accepted Lean results as proof-backed claims.

Risk: Cost and resource use can exceed the stated tier expectations because bandwidth, CPU, GPU, API calls, rate limits, samples, and rounds vary by run.

Mitigation: Start with minimal samples and rounds, record model and budget metadata beside each proof artifact, and quote measured run metadata rather than estimates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/exo-suite-linkage)
- [Publisher profile](https://clawhub.ai/user/diamond2nv)
- [Hermes homepage: omega-architect](https://github.com/diamond2nv/omega-architect)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and handoff checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory workflow instructions; generated artifacts from the referenced tools should carry identity, provenance, versions, models, seeds, and verification status.]

## Skill Version(s):

0.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
