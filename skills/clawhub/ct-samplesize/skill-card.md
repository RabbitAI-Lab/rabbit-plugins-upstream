## Description: <br>
ct-samplesize helps clinical trial practitioners calculate sample size, power, power curves, and related design outputs across 49 test types using natural-language prompts backed by local R/Python tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[medstatstar](https://clawhub.ai/user/medstatstar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External clinical researchers, biostatisticians, and trial teams use this skill to choose an appropriate test family and produce sample-size, power, curve, simulation, and reproducible-code outputs for clinical-trial planning. Outputs are planning aids and should be independently validated before protocol or regulatory use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run generated local R code when execution is explicitly confirmed. <br>
Mitigation: Use the default preview mode to inspect generated R code first, and execute only after confirming the parameters and code path. <br>
Risk: Optional CRAN package installation introduces package supply-chain and environment-change risk when --run-install is used. <br>
Mitigation: Install packages only from trusted repositories in a controlled R environment, and avoid --run-install when offline review or locked dependencies are required. <br>
Risk: Clinical-trial calculations may be used in protocol or regulatory planning where incorrect assumptions can materially affect decisions. <br>
Mitigation: Treat outputs as planning aids and require independent statistical review before using results in protocols, submissions, or operational decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-samplesize) <br>
- [Metadata Homepage](https://github.com/medstatstar/ct-samplesize) <br>
- [README](artifact/README.md) <br>
- [Operation SOP](artifact/references/operation_sop.md) <br>
- [CLI Examples](artifact/references/cli_examples.md) <br>
- [R Package Reference](artifact/references/r_packages.md) <br>
- [Formula Reference](artifact/references/formulas.md) <br>
- [Adaptive Simulator Reference](artifact/references/adaptive_simulator.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with calculated results, generated R code previews, optional shell commands, and optional PNG/JSON artifacts for curve or simulation workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default mode previews generated R code without execution; explicit confirmation is required to run local R calculations.] <br>

## Skill Version(s): <br>
3.8.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
