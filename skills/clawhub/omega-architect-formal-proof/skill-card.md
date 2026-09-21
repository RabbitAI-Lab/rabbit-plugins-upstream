## Description:

Formal theorem proving with omega-architect: install the CLI, configure a Lean 4 toolchain and an LLM backend, and drive the generate -> compile -> verify loop (`omega prove`), including strategy modes, budgets and no-LLM smoke tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up omega-architect, connect Lean 4 and an LLM backend, and run proof-search workflows that accept only Lean-compiled proof candidates. It is intended for theorem headers, invariants, bounds, type-level facts, and other statements that need machine-checked proof support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running a third-party proof-search CLI from GitHub may execute code and depend on external release artifacts.

Mitigation: Pin versions where possible, verify the upstream project and release artifacts, and use an isolated tool environment.

Risk: LLM-backed proof generation can consume API tokens or local model resources quickly as samples and rounds increase.

Mitigation: Start with low sample and round limits, set timeouts and budget controls, and measure local backend suitability before scaling.

Risk: Generated proof candidates may be incorrect or unverified if Lean is unavailable or compilation fails.

Mitigation: Treat only Lean-compiled proofs as verified and keep the statement, proof body, imports, model, and run parameters with each proof artifact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/omega-architect-formal-proof)
- [omega-architect repository](https://github.com/diamond2nv/omega-architect)
- [elan Lean toolchain](https://github.com/leanprover/elan)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and Lean theorem snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to install and configure tools, run proof-search commands, constrain budgets, and distinguish generated candidates from Lean-compiled verified proofs.]

## Skill Version(s):

0.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
